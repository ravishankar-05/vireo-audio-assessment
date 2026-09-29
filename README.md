# Vireo Audio AI Support Pipeline

## Setup Instructions
1. Ensure you have Python installed.
2. Install dependencies: `pip install pandas`
3. Place the provided CSV and PDF files into the `data/` directory.
4. Run the pipeline: `python main.py`

## Architecture & Business Logic
I pushed back on the client's request to build a dashboard penalizing agents. The data proves the CSAT drop is caused by defective manufacturing lots (PL2-2510 and PL2-2511), not agent performance. 

I used Pandas for deterministic data joins and financial calculations to find the exact financial bleed (₹16,08,421). To keep the operational cost at ₹0 for the client, I built a local keyword-heuristic pipeline using standard Python libraries rather than relying on external paid LLM calls to categorize a sample of the defective tickets.