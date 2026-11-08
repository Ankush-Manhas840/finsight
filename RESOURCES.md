# FinSight — Day-by-Day Study → Build Plan (Nov 1 – Dec 31, 2026)

**Rule for every day:** first do the **Study** part (≈1–1.5 h), then the **Build** part (≈1.5–2 h), then commit and write 2–3 lines in `LEARNINGS.md` (what broke, what you tried, what worked).
Keep ~1 h of DSA daily on top of this.

Buffer days are for catching up. If you are on track, use them to re-read your own code and explain it out loud.

---

## Week 1 (Nov 1–7): LLM basics + finance basics

| Day | Study first | Then build |
|---|---|---|
| **Nov 1** | [Karpathy: Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (1 h): what an LLM is, tokens, why it hallucinates | Get a free [Gemini API key](https://aistudio.google.com/), put it in `.env`, make `src/llm.py` print an answer to "What is revenue?". Use a **Flash** model and note your real free limits from [AI Studio rate limits](https://aistudio.google.com/rate-limit) |
| **Nov 2** | [Gemini API docs](https://ai.google.dev/gemini-api/docs): text generation, system instructions, structured output (JSON) | In `notebooks/01_llm_basics.ipynb`: ask for `{"metric": ..., "definition": ...}` as JSON and parse it into a Python dict |
| **Nov 3** | [Zerodha Varsity — Fundamental Analysis](https://zerodha.com/varsity/module/fundamental-analysis/), chapters 1–4 (annual report, P&L statement) | Download the FY2025 annual reports for **Maruti Suzuki, Mahindra & Mahindra, Bajaj Auto** from [BSE](https://www.bseindia.com/) or the company sites into `data/raw/`. Write their sources in `data/SOURCES.md` |
| **Nov 4** | Varsity chapters 5–7 (balance sheet, cash flow statement) | Open each PDF and find revenue, net profit and total debt yourself. Fill 10 rows of `eval/ground_truth.csv`, cross-checking on [Screener.in](https://www.screener.in/) |
| **Nov 5** | Varsity ratio chapters (profit margin, debt-to-equity, ROE, EPS) | Add 10 rows of ratios to `ground_truth.csv`. Write a 10-term finance glossary in `LEARNINGS.md` in your own words |
| **Nov 6** | [3Blue1Brown: Transformers explained](https://www.youtube.com/watch?v=wjZofJX0v4M) + [Sentence-Transformers quickstart](https://www.sbert.net/docs/quickstart.html) | `notebooks/02_embeddings.ipynb`: embed 10 finance sentences and print a cosine-similarity table. Check that "net profit" ≈ "PAT" |
| **Nov 7** | *Buffer.* Re-read your notes | Download FY2023 + FY2024 reports too (9 PDFs total). Write week 1 in `LEARNINGS.md` |

## Week 2 (Nov 8–14): LangChain + your first RAG

| Day | Study first | Then build |
|---|---|---|
| **Nov 8** | [DeepLearning.AI: LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/), lessons 1–3 | Rewrite `src/llm.py` to use a LangChain chat model + prompt template |
| **Nov 9** | Same course, lessons 4–6 (chains, Q&A over documents, evaluation) | `notebooks/03_pdf_loading.ipynb`: load one annual report with `PyPDFLoader`, print 3 pages, and notice how badly the tables come out |
| **Nov 10** | [LangChain docs](https://docs.langchain.com/) (search "text splitters"). What chunk size and overlap mean | `src/ingest.py`: load all PDFs and split them into chunks with metadata `{company, year, page}` |
| **Nov 11** | [Chroma docs: getting started](https://docs.trychroma.com/) | `src/vectorstore.py`: embed the chunks into a persistent Chroma DB, then run a similarity search for "total borrowings" |
| **Nov 12** | [LangChain docs](https://docs.langchain.com/) (search "RAG tutorial") | `src/rag.py`: retrieve top-k chunks, answer, and cite `(company, year, page)` |
| **Nov 13** | Re-read your code end to end | Make `python -m src.rag "question"` work. Ask 10 questions and log every wrong answer in `LEARNINGS.md` |
| **Nov 14** | *Buffer* | Clean up the code and update the README "How to run" section |

## Week 3 (Nov 15–21): Evals, the part that makes you stand out

| Day | Study first | Then build |
|---|---|---|
| **Nov 15** | [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) | `eval/questions.jsonl`: 30 questions with the expected answer and source page, using your ground truth |
| **Nov 16** | [DeepLearning.AI: Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/), lessons 1–2 | `eval/eval_retrieval.py`: hit rate@k (did the correct page get retrieved?) |
| **Nov 17** | Learn how to compare numbers with a tolerance and parse "₹1,23,456 crore" | `eval/eval_numbers.py`: % of answers whose number is within 1% of the truth |
| **Nov 18** | [RAGAS docs](https://docs.ragas.io/): faithfulness, answer relevancy | Add a RAGAS faithfulness run to the eval script. RAGAS makes many LLM calls per question, so **cache LLM answers to disk** first or you will burn the free quota |
| **Nov 19** | — | **Run baseline v1.** Put the scores in the README results table. Sort failures into types: table misread, wrong year, wrong company, made-up number |
| **Nov 20** | — | Grow the set to 50 questions, including tricky ones (standalone vs consolidated, FY naming) |
| **Nov 21** | *Buffer* | Week 3 in `LEARNINGS.md`: which failure type is most common? |

## Week 4 (Nov 22–28): Fixing retrieval (v1 → v3)

| Day | Study first | Then build |
|---|---|---|
| **Nov 22** | [Docling docs](https://docling-project.github.io/docling/): PDF tables to markdown | `src/ingest.py`: parse with Docling and keep tables as markdown |
| **Nov 23** | Chunking strategies (same Advanced RAG course, lesson 3) | Table-aware chunking: keep each table whole with its heading. **Rerun evals (v2)** |
| **Nov 24** | [Chroma metadata filtering](https://docs.trychroma.com/) | Get the LLM to extract `{company, year}` from the question and filter retrieval with it |
| **Nov 25** | [Pinecone: Hybrid search](https://docs.pinecone.io/guides/search/hybrid-search) (BM25 + vectors) | Hybrid retriever: BM25 + vector search combined |
| **Nov 26** | [Sentence-Transformers: cross-encoders / rerankers](https://www.sbert.net/docs/cross_encoder/usage/usage.html) | Add a reranker (`BAAI/bge-reranker-base`) on the top 20 results |
| **Nov 27** | [Anthropic: Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval) | Add a context header to each chunk ("Maruti FY24, Balance Sheet"). **Rerun evals (v3)** and fill in the v1→v2→v3 table |
| **Nov 28** | *Buffer* | `LEARNINGS.md`: which fix helped the most, and why? |

## Week 5 (Nov 29–Dec 5): Qdrant + agents

| Day | Study first | Then build |
|---|---|---|
| **Nov 29** | [Qdrant quickstart](https://qdrant.tech/documentation/quickstart/) + Docker basics | Run Qdrant with `docker compose up -d`, swap Chroma for Qdrant, and check that the eval scores stay the same |
| **Nov 30** | [DeepLearning.AI: AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/), lessons 1–2 | `notebooks/04_toy_agent.ipynb`: an agent with one calculator tool |
| **Dec 1** | [LangChain Academy: Intro to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph), module 1 | `src/tools/retriever_tool.py`: wrap your retriever as a tool |
| **Dec 2** | Python `pytest` refresher | `src/tools/calculator.py`: margin, debt-to-equity and YoY growth as functions, plus tests (**the LLM must never do the maths itself**) |
| **Dec 3** | Same LangGraph course, lessons 3–4 | `src/agent.py`: a graph that goes understand → retrieve → calculate → answer |
| **Dec 4** | LangChain Academy module 2 (state, memory) | Make comparison questions work, e.g. "Compare M&M and Maruti margin FY23–FY25" |
| **Dec 5** | *Buffer* | Week 5 in `LEARNINGS.md` |

## Week 6 (Dec 6–12): Making the agent trustworthy

| Day | Study first | Then build |
|---|---|---|
| **Dec 6** | Matplotlib refresher | `src/tools/chart.py`: a multi-year comparison chart tool |
| **Dec 7** | Read about hallucination and guardrails (Hamel's blog + the Advanced RAG course) | **Number verification:** every number in the answer must appear in a retrieved chunk or a calculator output, otherwise it gets flagged |
| **Dec 8** | — | **Guardrails:** refuse investment-advice and off-topic questions, and answer "not found in the report" when no retrieved page supports the answer, with tests |
| **Dec 9** | — | Add 20 agent questions (comparisons, ratios) to the eval set |
| **Dec 10** | — | **Full eval run (v4)** and update the README table |
| **Dec 11** | [LangSmith docs](https://docs.langchain.com/langsmith/observability) (free: 5,000 traces/month) or plain logging | **Monitoring:** log every query (question, pages found, answer, tokens, latency, cost) to a file, and add averages to the README |
| **Dec 12** | Read about caching LLM calls | **Cache and router:** save answers so a repeated question costs nothing, and send easy questions to the cheaper model (flash-lite); measure the money saved. Then `LEARNINGS.md` |

## Week 7 (Dec 13–19): API, UI, Docker, deploy

| Day | Study first | Then build |
|---|---|---|
| **Dec 13** | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) (you know this from the fraud project) | `src/api/main.py`: `/health` and `/ask` endpoints |
| **Dec 14** | — | Pydantic schemas + `tests/test_api.py` |
| **Dec 15** | [Streamlit: build a chat app](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps) | `app/streamlit_app.py`: a chat UI that shows citations and charts |
| **Dec 16** | — | Upload a new annual report from the UI and ingest it on the fly |
| **Dec 17** | [Docker: containerize a Python app](https://docs.docker.com/guides/python/) | A `Dockerfile` + compose setup running api + qdrant + ui |
| **Dec 18** | [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud) + [Qdrant Cloud free cluster](https://qdrant.tech/documentation/cloud/) | Build the index **on your own PC** (Docling and the reranker are too heavy for ~1 GB RAM), upload vectors to Qdrant Cloud, deploy the Streamlit app. Open the Qdrant cluster weekly or it gets paused. *(Hugging Face Docker/Gradio Spaces now need a paid plan; Render's 512 MB is too small.)* |
| **Dec 19** | *Buffer* | Fix whatever broke in deployment |

## Week 8 (Dec 20–26): Polish + showcase

| Day | Do |
|---|---|
| **Dec 20** | Add 2 more companies and check that everything still works and scores hold |
| **Dec 21** | Architecture diagram + final README results table |
| **Dec 22** | Move settings to `config/config.yaml`, clean up tests and logging |
| **Dec 23** | Blog post: "What broke when I built RAG over Indian annual reports" (use `LEARNINGS.md`) |
| **Dec 24** | Record a 2-minute demo video or GIF |
| **Dec 25** | *Buffer* |
| **Dec 26** | LinkedIn post, pin the repo, add resume bullets with numbers |

## Dec 27–31: Interview prep on your own project
Ask Claude to mock-interview you on FinSight using `LEARNINGS.md`, covering chunking choices, why hybrid search, how evals work and the failure cases. Practise a 2-minute spoken walkthrough.

---

## Backup resources (if a concept doesn't click)
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) and [Agents Course](https://huggingface.co/learn/agents-course)
- [Groq](https://console.groq.com/) (free with per-model rate limits, fast open models) or [Ollama](https://ollama.com/) (run models locally) if the Gemini free tier runs out
- Ask Claude: "explain X like I'm new, then quiz me"

> Library docs change often (especially LangChain). If a link moves, search for the page title.
