### What did you build, and what business outcome does it move?
Built a Python-based data pipeline and local heuristic categorizer. It shifts the outcome from "wasting Q3 budget on unnecessary agent training" to "identifying and recalling defective Lots PL2-2510 and PL2-2511." This proves the CSAT drop is a hardware issue, saving roughly ₹16 Lakhs in ongoing operational bleed.

### What does one run cost, and what would a month cost at Vireo's volume (roughly 650 tickets a week)?
₹0. To keep operational costs at absolute zero for the client, I built a local keyword-heuristic pipeline using standard Python libraries rather than relying on external paid LLM API calls. Processing 2,600 tickets a month will cost nothing in API fees.

### How do you know it works?
Sample size tested: 30 tickets. I manually audited the tickets against the script's classification. The local heuristic correctly identified hardware defects with high accuracy, capturing the most common customer phrasing (e.g., "dead", "left earbud").

### Did you change, narrow, or push back on the client's ask?
Yes. I pushed back on building an agent-level CSAT dashboard. The data indicates CSAT drops are tied strictly to product defects in specific lots, not agent performance. Retraining agents would burn the Q3 budget without solving the root cause.

### What is wrong with what you are handing us?
To respect the 5-hour limit and avoid API dependencies, the text categorization uses a hardcoded keyword heuristic rather than a robust NLP model. It will struggle with sarcasm or complex multi-intent emails. The script is also not containerized.

### What did you deliberately leave out, and why that rather than something else?
I left out a visual dashboard interface (React/Streamlit). I prioritized the deterministic Pandas data pipeline and the business analysis over UI, because a pretty dashboard showing the wrong business conclusion (penalizing agents) is actively harmful.

### Anything you built or found that nobody asked for?
I calculated the exact financial bleed (₹16,08,421) caused by the defective lots by cross-referencing the unit costs in `products.csv` and the logistics rules in the `support-policy.pdf`.

### What did you use AI for?
I used an AI assistant strictly as a thought partner to help structure the Pandas join logic rapidly. I intentionally built the final script *without* external LLM API dependencies to demonstrate a ₹0 operational cost solution. Link to screen recording: [Insert Link]

### Your Public Google Drive Link
[Insert Link]

### Someone picks this up on Monday and you are unreachable. The three things they need to know.
1. Drop all the raw CSVs into the `data/` folder.
2. Run `pip install pandas`.
3. Run `python main.py`. The categorization output saves to `data/categorized_sample.csv`.

### Honest hours spent.
4.5

### Github Repo Link
[Insert Link]