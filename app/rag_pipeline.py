from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def build_retriever(raw_docs):
    docs = [Document(page_content=d) for d in raw_docs]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    splits = splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=OllamaEmbeddings(model="nomic-embed-text")
    )

    return vectorstore.as_retriever(search_kwargs={"k": 4})
