# main.py
from langgraph.graph import StateGraph, START, END
from mcp_tools.arxiv_tool import fetch_arxiv_papers
from agents.summarizer_agent import summarize_text
from agents.cluster_agent import cluster_summaries

def build_graph():
    graph = StateGraph(dict)

    def retriever(state):
        query = state["query"]
        print(f"\n Fetching papers for topic: {query} ...")
        papers = fetch_arxiv_papers(query, max_results=5)
        return {"papers": papers}

    def summarizer(state):
        papers = state["papers"]
        print("\n Summarizing abstracts...\n")
        summaries = []
        for p in papers:
            summary = summarize_text(p["summary"])
            summaries.append({
                "title": p["title"],
                "authors": p["authors"],
                "link": p["link"],
                "summary": summary
            })
        return {"summaries": summaries}

    def clusterer(state):
        summaries = state["summaries"]
        print("\n🔗 Clustering papers by topic...\n")
        clusters = cluster_summaries(summaries, n_clusters=3)
        return {"clusters": clusters}

    graph.add_node("retriever", retriever)
    graph.add_node("summarizer", summarizer)
    graph.add_node("clusterer", clusterer)

    graph.add_edge(START, "retriever")
    graph.add_edge("retriever", "summarizer")
    graph.add_edge("summarizer", "clusterer")
    graph.add_edge("clusterer", END)

    return graph.compile()

def main():
    query = input("Enter your research topic: ")
    app = build_graph()
    final_state = app.invoke({"query": query})
    clusters = final_state["clusters"]

    print("\n ===== Clustered Research Papers =====\n")
    for cluster_id, papers in clusters.items():
        print(f"\n Cluster {cluster_id + 1}:")
        for p in papers:
            print(f" • {p['title']} ({', '.join(p['authors'])})")
            print(f"   {p['summary']}\n")

if __name__ == "__main__":
    main()
