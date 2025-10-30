from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

def summarize_and_store(papers):
    """Summarizes papers and builds a retriever."""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    embeddings = OpenAIEmbeddings()
    docs = [Document(page_content=p) for p in papers]
    vectorstore = FAISS.from_documents(docs, embeddings)
    
    prompt = PromptTemplate.from_template(
        "Summarize the following research paper:\n\n{text}\n\nSummary:"
    )
    chain = prompt | llm
    summaries = [chain.invoke({"text": d.page_content}).content for d in docs]
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    return summaries, retriever

def ask_question(retriever, question):
    """Queries the RAG pipeline."""
    llm = ChatOpenAI(model="gpt-4o-mini")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(question)
