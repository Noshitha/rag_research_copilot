# agents/cluster_agent.py
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

def cluster_summaries(summaries, n_clusters=3):
    """
    Clusters paper summaries into topic groups using semantic embeddings.
    Returns cluster labels and grouped summaries.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    texts = [s["summary"] for s in summaries]
    embeddings = model.encode(texts, convert_to_tensor=False)

    n_clusters = min(n_clusters, len(summaries))  # safe bound
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(embeddings)

    clustered = {}
    for idx, label in enumerate(labels):
        clustered.setdefault(int(label), []).append(summaries[idx])

    return clustered
