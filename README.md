# FinSight — Annual Report Analyst Agent

Ask questions about Indian listed companies in plain English ("Compare Maruti and M&M profit margins FY23–FY25") and get answers with **page citations**, **numbers calculated by code (not guessed by the LLM)**, and charts. Accuracy is measured with an evaluation set.

## Architecture

```
Annual report PDFs (BSE) → Docling parsing (tables → markdown)
                                    │
                         chunks + metadata {company, year, page}
                                    │
                    embeddings → Qdrant (vector DB) + BM25 index
                                    │
 Question → LangGraph agent ── retriever tool (hybrid search + reranker)
                          ├── calculator tool (ratios, growth)
                          ├── chart tool
                          └── number verification → answer + citations
                                    │
                    FastAPI /ask  →  Streamlit chat UI
                                    │
                    eval/ : retrieval hit-rate, numeric accuracy, faithfulness
```

## Tech stack

| Area | Tool |
|---|---|
| Language | Python 3.10+ |
| LLM | Gemini API Flash (free tier); Groq / Ollama as backup |
| Framework | LangChain, LangGraph |
| PDF parsing | PyPDF → Docling |
| Embeddings / reranker | sentence-transformers, `BAAI/bge-reranker-base` |
| Vector DB | Chroma (start) → Qdrant (via Docker) |
| Keyword search | BM25 (`rank-bm25`) |
| Evals | custom scripts + RAGAS |
| API / UI | FastAPI, Streamlit |
| Testing | pytest |
| Containers | Docker, Docker Compose |
| Deploy (free) | Streamlit Community Cloud + Qdrant Cloud free cluster |

## Data

FY2023–FY2025 annual reports of **Maruti Suzuki, Mahindra & Mahindra, Bajaj Auto** from [BSE](https://www.bseindia.com/). PDFs are **not committed**; sources are listed in `data/SOURCES.md`. Ground-truth numbers are cross-checked against [Screener.in](https://www.screener.in/).

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env        # then paste your API key
```

## How to run

- Ingest PDFs: _TODO_
- Ask a question: _TODO_
- Run evals: _TODO_
- Start API + UI: _TODO_

## Results

| Version | Change | Retrieval hit@5 | Numeric accuracy | Faithfulness |
|---|---|---|---|---|
| v1 | naive RAG (PyPDF + Chroma) | | | |
| v2 | Docling tables + table-aware chunks | | | |
| v3 | metadata filter + hybrid + reranker | | | |
| v4 | agent + calculator + number verification | | | |

## Progress

Detailed study links for each day are in [RESOURCES.md](RESOURCES.md).

### Week 1 — LLM + finance basics
- [ ] **Nov 1** — LLM hello world `[feat: add llm client]`
- [ ] **Nov 2** — Structured JSON output `[feat: add structured output notebook]`
- [ ] **Nov 3** — Download FY25 reports `[docs: add data sources]`
- [ ] **Nov 4** — 10 ground-truth numbers `[feat: add ground truth]`
- [ ] **Nov 5** — Ratios + glossary `[docs: add finance glossary]`
- [ ] **Nov 6** — Embeddings notebook `[feat: add embeddings notebook]`
- [ ] **Nov 7** — FY23/24 reports. *Buffer*
### Week 2 — LangChain + first RAG
- [ ] **Nov 8** — LangChain chat model `[refactor: use langchain llm]`
- [ ] **Nov 9** — PDF loading notebook `[feat: add pdf loading notebook]`
- [ ] **Nov 10** — Chunking with metadata `[feat: add ingestion]`
- [ ] **Nov 11** — Chroma vector store `[feat: add chroma store]`
- [ ] **Nov 12** — RAG with citations `[feat: add rag pipeline]`
- [ ] **Nov 13** — CLI + first failure log `[feat: add rag cli]`
- [ ] **Nov 14** — *Buffer*
### Week 3 — Evals
- [ ] **Nov 15** — 30 eval questions `[feat: add eval set]`
- [ ] **Nov 16** — Retrieval hit-rate `[feat: add retrieval eval]`
- [ ] **Nov 17** — Numeric accuracy `[feat: add numeric eval]`
- [ ] **Nov 18** — RAGAS faithfulness `[feat: add ragas eval]`
- [ ] **Nov 19** — Baseline v1 results `[docs: add v1 results]`
- [ ] **Nov 20** — 50 questions `[feat: expand eval set]`
- [ ] **Nov 21** — *Buffer*
### Week 4 — Better retrieval
- [ ] **Nov 22** — Docling parsing `[feat: parse tables with docling]`
- [ ] **Nov 23** — Table-aware chunks, v2 `[feat: table-aware chunking]`
- [ ] **Nov 24** — Metadata filtering `[feat: add metadata filters]`
- [ ] **Nov 25** — Hybrid search `[feat: add hybrid retriever]`
- [ ] **Nov 26** — Reranker `[feat: add reranker]`
- [ ] **Nov 27** — Contextual chunks, v3 `[feat: add contextual headers]`
- [ ] **Nov 28** — *Buffer*
### Week 5 — Qdrant + agent
- [ ] **Nov 29** — Swap to Qdrant `[feat: move to qdrant]`
- [ ] **Nov 30** — Toy agent `[feat: add toy agent notebook]`
- [ ] **Dec 1** — Retriever tool `[feat: add retriever tool]`
- [ ] **Dec 2** — Calculator tool + tests `[feat: add calculator tool]`
- [ ] **Dec 3** — LangGraph agent `[feat: add langgraph agent]`
- [ ] **Dec 4** — Multi-company comparisons `[feat: support comparisons]`
- [ ] **Dec 5** — *Buffer*
### Week 6 — Trustworthy agent
- [ ] **Dec 6** — Chart tool `[feat: add chart tool]`
- [ ] **Dec 7** — Number verification `[feat: add number verification]`
- [ ] **Dec 8** — Refusals + tests `[feat: add guardrails]`
- [ ] **Dec 9** — Agent eval questions `[feat: add agent evals]`
- [ ] **Dec 10** — v4 results `[docs: add v4 results]`
- [ ] **Dec 11** — Cost + latency tracking `[feat: add usage tracking]`
- [ ] **Dec 12** — *Buffer*
### Week 7 — Ship it
- [ ] **Dec 13** — FastAPI `/ask` `[feat: add api]`
- [ ] **Dec 14** — Schemas + API tests `[test: add api tests]`
- [ ] **Dec 15** — Streamlit chat UI `[feat: add chat ui]`
- [ ] **Dec 16** — Upload + ingest `[feat: add upload]`
- [ ] **Dec 17** — Docker `[chore: add docker]`
- [ ] **Dec 18** — Deploy to Streamlit Cloud + Qdrant Cloud `[chore: deploy demo]`
- [ ] **Dec 19** — *Buffer*
### Week 8 — Showcase
- [ ] **Dec 20** — 2 more companies `[feat: add companies]`
- [ ] **Dec 21** — Diagram + results `[docs: final results]`
- [ ] **Dec 22** — Config + cleanup `[refactor: config and cleanup]`
- [ ] **Dec 23** — Blog post
- [ ] **Dec 24** — Demo video
- [ ] **Dec 26** — LinkedIn, pin repo, resume
- [ ] **Dec 27–31** — Mock interviews on this project

## Future work

- Link with fraud-detection-realtime (agent explains flagged transactions)
- MCP server exposing the tools
- Fine-tuned small model for metric extraction
