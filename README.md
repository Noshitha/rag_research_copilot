# RAG-based Research Copilot :

An intelligent multi-agent research assistant built with **LangGraph**, **LangChain**, and **Model Context Protocol (MCP)** to automate literature exploration. It retrieves papers, summarizes key insights, clusters related works, and visualizes research trends.

---

## Key Highlights
-  **Retrieval Agent:** Queries and extracts papers from *arXiv* using a custom **MCP** integration.  
-  **Summarization Agent:** Performs on-device abstractive summarization via **Hugging Face BART-large-CNN** (no API calls or cost).  
-  **Clustering Agent:** Uses **Sentence-BERT embeddings** + **K-Means** to group related papers by topic and generate 2-D projections.  
-  **Visualization Layer:** Built with **Streamlit** + **Plotly**, producing an interactive dashboard with topic clusters and summaries.  
-  **LangGraph Workflow:** Manages agent state transitions (retriever -> summarizer -> clusterer) for modular, debuggable execution.  
-  **Offline & Extensible:** Runs locally on CPU/GPU (MPS supported) and easily extendable with new MCP tools.

---

## Architecture :
                          ┌──────────────────────────────────────┐
                          │         User Query Input             │
                          │  (e.g., "Multilingual Translation")  │
                          └──────────────────────────────────────┘
                                             │
                                             ▼
                     ┌────────────────────────────────────────┐
                     │  Retriever Agent (LangGraph Node 1)    │
                     │  → fetch_arxiv_papers() via MCP        │
                     │  → Retrieves 3–5 recent papers         │
                     └────────────────────────────────────────┘
                                             │
                                             ▼
                     ┌───────────────────────────────────────────┐
                     │ Summarizer Agent (LangGraph Node 2)       │
                     │  → Local BART summarizer (HuggingFace)    │
                     │  → On-device MPS inference (no API)       │
                     │  → Outputs concise 2–3 sentence summaries │
                     └───────────────────────────────────────────┘
                                             │
                                             ▼
                     ┌────────────────────────────────────────┐
                     │ Cluster Agent (LangGraph Node 3)       │
                     │  → Sentence-BERT embeddings            │
                     │  → KMeans + PCA 2-D projection         │
                     │  → Groups similar papers by topic      │
                     └────────────────────────────────────────┘
                                             │
                                             ▼
                     ┌────────────────────────────────────────┐
                     │ Streamlit Dashboard                    │
                     │  → Displays clusters & summaries       │
                     │  → Plotly scatterplot visualization    │
                     │  → Allows export (optional next)       │
                     └────────────────────────────────────────┘


## Installation :
```bash
git clone https://github.com/Noshitha98/rag_research_copilot.git
```

## Streamlit deployment:
<img width="1070" height="498" alt="image" src="https://github.com/user-attachments/assets/2876869d-8b62-43a7-97b5-abf9a31b4dda" />
