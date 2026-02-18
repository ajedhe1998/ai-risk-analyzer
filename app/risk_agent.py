from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def create_risk_agent(retriever):
    llm = Ollama(model="phi3")

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    return chain
