# End-to-End RAG App with Streamlit + LangChain + Pinecone + HuggingFace
import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone as PineconeStore
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import pinecone
from dotenv import load_dotenv

load_dotenv()

# ----------- CONFIG ----------- #
PINECONE_API_KEY = "pcsk_3LviPv_CutrK4iiyr5BSkokemdLGVBNC3r3Uz1hrhPnMpKuNHh6wd9k8SdoQvZQ3cDVVZr"
PINECONE_ENV = "llama-text-embed-v2"
INDEX_NAME = "demo"

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# ----------- INIT EMBEDDINGS ----------- #
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

# ----------- INIT PINECONE ----------- #
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
if INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(INDEX_NAME, dimension=384)
index = pinecone.Index(INDEX_NAME)

# ----------- DOC LOAD AND INGEST ----------- #
def ingest_docs(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    PineconeStore.from_documents(chunks, embeddings, index_name=INDEX_NAME)

# ----------- RAG CHAIN ----------- #
def get_qa_chain():
    vectorstore = PineconeStore(index, embeddings, index_name=INDEX_NAME)
    retriever = vectorstore.as_retriever()

    llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

# ----------- STREAMLIT APP ----------- #
st.set_page_config(page_title="RAG Q&A App")
st.title("📚 Retrieval-Augmented Generation App")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF document", type="pdf")
if uploaded_file is not None:
    with open("temp_doc.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("Document uploaded. Now processing...")
    ingest_docs("temp_doc.pdf")
    st.success("Document processed and indexed!")

# User Query
query = st.text_input("Ask a question based on your document:")
if query:
    qa = get_qa_chain()
    result = qa(query)
    st.subheader("Answer")
    st.write(result["result"])

    with st.expander("📄 Source Documents"):
        for doc in result["source_documents"]:
            st.markdown(f"**Source:** {doc.metadata['source']}")
            st.write(doc.page_content[:300] + "...")

# ----------- END ----------- #
