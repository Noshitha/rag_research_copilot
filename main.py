from mcp_tools.arxiv_tool import fetch_arxiv_papers
from agents.summarizer_agent import summarize_and_store, ask_question

def main():
    query = "large language models for translation"
    raw_papers = fetch_arxiv_papers(query)
    summaries, retriever = summarize_and_store([raw_papers])
    
    print("=== Summaries ===")
    for s in summaries:
        print("-", s, "\n")
    
    print("=== QA Demo ===")
    ans = ask_question(retriever, "What are common model compression methods in LLMs?")
    print(ans)

if __name__ == "__main__":
    main()
