import pandas as pd

def run_pipeline():
    print("Loading data...")
    try:
        tickets = pd.read_csv("data/tickets.csv")
        orders = pd.read_csv("data/orders.csv")
        products = pd.read_csv("data/products.csv")
    except FileNotFoundError:
        print("Error: Make sure tickets.csv, orders.csv, and products.csv are in the 'data' folder.")
        return

    # Merge to find the bad lot
    merged = tickets.dropna(subset=['order_id']).merge(orders, on='order_id', how='left')
    merged = merged.merge(products, on='sku', how='left')
    
    # Identify the problematic lots
    is_bad_lot = merged['lot_code'].astype(str).str.startswith(('PL2-2510', 'PL2-2511'))
    bad_lots = merged.loc[is_bad_lot]
    
    print("\n--- BUSINESS IMPACT ---")
    print(f"Overall Average CSAT: {merged['csat_score'].mean():.2f}")
    print(f"CSAT for Bad Lots (PL2 Oct/Nov): {bad_lots['csat_score'].mean():.2f}")
    
    # Calculate costs (Unit cost + ₹340 logistics per policy)
    replacements = bad_lots[bad_lots['replacement_issued'] == 'Y']
    replacement_cost = (replacements['unit_cost_inr'] + 340).sum()
    refunds = bad_lots['refund_amount_inr'].sum()
    support_cost = bad_lots.shape[0] * 290 # ₹290 per contact
    
    total_bleed = replacement_cost + refunds + support_cost
    print(f"Total Financial Bleed from Bad Lots: ₹{total_bleed:,.2f}")

    print("\n--- LOCAL NLP CATEGORIZATION (30 TICKET SAMPLE) ---")
    sample = bad_lots.dropna(subset=['customer_message']).sample(n=30, random_state=42)
    
    results = []
    for _, row in sample.iterrows():
        text = str(row['customer_message']).lower() + " " + str(row.get('agent_notes', '')).lower()
        
        # Local heuristic mimicking intent extraction
        if any(word in text for word in ['dead', 'left', 'right', 'broken', 'charge', 'stop', 'working', 'connect']):
            cat = "Hardware Defect"
        elif any(word in text for word in ['deliver', 'late', 'track', 'missing', 'courier']):
            cat = "Delivery Issue"
        elif any(word in text for word in ['policy', 'refund', 'manager', 'escalate']):
            cat = "Policy Friction"
        else:
            cat = "Other"
            
        results.append({'ticket_id': row['ticket_id'], 'category': cat})
    
    df_results = pd.DataFrame(results)
    df_results.to_csv("data/categorized_sample.csv", index=False)
    print("Categorization saved to data/categorized_sample.csv")

if __name__ == "__main__":
    run_pipeline()