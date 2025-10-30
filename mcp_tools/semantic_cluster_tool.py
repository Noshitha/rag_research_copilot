from langchain_mcp_adapters import register_tool
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

@register_tool
def cluster_texts(texts: list, n_clusters: int = 5):
    """Clusters text embeddings into semantic groups."""
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)
    return {i: [] for i in range(n_clusters)} | {f"cluster_{l}": t for t, l in zip(texts, labels)}
