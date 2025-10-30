# app.py
import streamlit as st
from mcp_tools.arxiv_tool import fetch_arxiv_papers
from agents.summarizer_agent import summarize_text
from agents.cluster_agent import cluster_summaries

st.set_page_config(page_title="RAG Research Copilot", layout="wide")

st.title("  RAG-based Research Copilot")
topic = st.text_input("Enter a research topic:", "multilingual machine translation")

if st.button(" Search & Summarize"):
    with st.spinner("Fetching papers..."):
        papers = fetch_arxiv_papers(topic, max_results=5)

    with st.spinner("Summarizing papers..."):
        summaries = []
        for p in papers:
            summary = summarize_text(p["summary"])
            summaries.append({
                "title": p["title"],
                "authors": p["authors"],
                "link": p["link"],
                "summary": summary
            })

    with st.spinner("Clustering topics..."):
        clusters = cluster_summaries(summaries, n_clusters=3)

    st.success(" Done! Explore clusters below:")

    for cluster_id, group in clusters.items():
        st.markdown(f"###  Cluster {cluster_id + 1}")
        for paper in group:
            st.markdown(f"**[{paper['title']}]({paper['link']})**")
            st.caption(f"Authors: {', '.join(paper['authors'])}")
            st.write(paper["summary"])
            st.divider()
