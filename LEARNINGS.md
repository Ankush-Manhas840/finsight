# LEARNINGS

Every day: what broke, what I tried, what worked. This file is my interview script.

## Finance glossary (Nov 5)

## Week 1


## Week 2: first RAG run (Nov 13)

Pipeline: 12 reports → 3,629 pages → 24,659 pieces (800 characters, 100 overlap) → Chroma with all-MiniLM-L6-v2 → top 5 pieces → Gemini 3.5 Flash Lite with "answer only from these pieces, cite pages, else say Not found".

| Question | Result | Why |
|---|---|---|
| Bajaj revenue FY2025 | Correct: 50,010 crore | Right pieces found |
| Maruti net profit FY2025 | Wrong: 142,976 million (key: 139,552) | Came from the FY2026 report, where FY2025 is **restated** (marked with a star) after a merger. Newer reports change old numbers. |
| Mahindra revenue FY2025 | "Not found" (answer is on page 150) | Search returned pages that only matched the word "Mahindra"; number tables give poor embeddings |
| Tesla profit | Correct: "Not found in the reports" | The refusal rule works |

Score: 2 of 4. Gemini behaved well every time; the failures are all in **search**.
Fixes already planned: read tables properly (Nov 22), filter by company and year (Nov 24), add keyword search (Nov 25).

Speed: each run takes about 20 seconds, of which 17 are Python loading libraries. The search itself is 0.3 seconds. A server that stays running (Dec 13) fixes this.
