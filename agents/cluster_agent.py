from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def build_cluster(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(docs, embeddings)
    return vectorstore
