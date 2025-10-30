# mcp_tools/arxiv_tool.py
import requests
import xml.etree.ElementTree as ET

def fetch_arxiv_papers(query: str, max_results: int = 5):
    """
    Fetches paper titles, authors, and summaries from arXiv based on a search query.
    Returns a list of dicts: [{title, authors, summary, link}, ...]
    """
    base_url = "http://export.arxiv.org/api/query"
    url = f"{base_url}?search_query=all:{query}&start=0&max_results={max_results}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    root = ET.fromstring(response.text)
    ns = {"arxiv": "http://www.w3.org/2005/Atom"}

    papers = []
    for entry in root.findall("arxiv:entry", ns):
        title = entry.find("arxiv:title", ns).text.strip()
        authors = [a.find("arxiv:name", ns).text for a in entry.findall("arxiv:author", ns)]
        summary = entry.find("arxiv:summary", ns).text.strip()
        link = entry.find("arxiv:id", ns).text.strip()

        papers.append({
            "title": title,
            "authors": authors,
            "summary": summary,
            "link": link
        })

    return papers

if __name__ == "__main__":
    query = "large language models"
    results = fetch_arxiv_papers(query)
    for i, p in enumerate(results, 1):
        print(f"\n{i}. {p['title']}\nAuthors: {', '.join(p['authors'])}\nSummary: {p['summary'][:300]}...\nLink: {p['link']}\n")
