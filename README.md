# RAG-based Research Copilot :

An intelligent multi-agent research assistant built with **LangGraph**, **LangChain**, and **Model Context Protocol (MCP)** to automate literature exploration. It retrieves papers, summarizes key insights, clusters related works, and visualizes research trends.

---

## Features :
- 🔍 **Paper Retrieval** — Fetch papers via arXiv or Semantic Scholar (MCP-integrated tools).  
- 🧠 **LLM Summarization** — Generate concise summaries using LangChain RAG pipelines.  
- 📊 **Topic Clustering** — Embed and group papers via FAISS + t-SNE.  
- 🕸️ **Agentic Workflow** — Managed by LangGraph for modular orchestration.  
- 🖥️ **Visualization** — Interactive Streamlit dashboard for exploring topics and insights.

---

## Architecture :
User Query
↓
Retriever Agent → (MCP: arXiv Tool)
↓
Summarizer Agent → (LangChain RAG)
↓
Cluster Agent → (MCP: Semantic Clustering)
↓
Visualizer Agent → Streamlit Dashboard

## Tech Stack :
- **LLM:** GPT-4 / Claude / local model  
- **Frameworks:** LangGraph, LangChain  
- **Tool Protocol:** langchain-mcp-adapters  
- **Vector Store:** FAISS  
- **UI:** Streamlit or Gradio  

## Installation :
```bash
git clone https://github.com/Noshitha98/rag_research_copilot.git
```
