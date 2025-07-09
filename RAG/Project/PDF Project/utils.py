import pinecone
from langchain.vectorstores import pinecone , FAISS
import langchain 
from langchain.document_loaders import PyPDFDirectoryLoader , CSVLoader , UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os 
from langchain.chains.question_answering import load_qa_chain

############################################################################
# Loader Section 
############################################################################

## PDF Loader 
def read_pdf(directory):
    """_summary_
    Args:
        directory (type:string): "it takes path of PDF file"
    Returns:
        (type:string): "it returns whole PDF content"
        
    """   
    file_loader=PyPDFDirectoryLoader(directory)
    documents=file_loader.load()
    return documents


## Word Document Loader 
def read_doc(directory):
    """_summary_
        Args:
            directory (type:string): "it takes path of Word file"
        Returns:
            (type:string): "it returns whole Word content"
    """
    file_loader=UnstructuredWordDocumentLoader(directory)
    document=file_loader.load()
    return document

## CSV Document Loader 
def read_csv(directory):
    """_summary_
        Args:
            directory (type:string): "it takes path of CSV file"
        Returns:
            (type:string): "it returns whole CSV content"
    """
    file_loader=CSVLoader(directory)
    document=file_loader.load()
    return document


############################################################################
# Text Splitting (Text Chunk)
############################################################################


## Divide the docs into chunks
def chunk_data(docs,chunk_size=800,chunk_overlap=50):
    """_summary_

    Args:
        docs (string): "any document or string which you want to splitting"
        chunk_size (int, optional): "Chunk Size in numbers" Defaults to 800.
        chunk_overlap (int, optional): "Chunk Overlap in numbers" Defaults to 50.

    Returns:
        list of string: "it return the chunks of the entire document in list of string
    """    
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    doc=text_splitter.split_documents(docs)
    return docs

############################################################################
# Embedding (FAISS,Pinecone)
############################################################################


def embedding_FAISS(embedding_model,chunks):
    """This function takes embedding model and chunks ,based on it returns FAISS vector store

    Args:
        embedding_model (model): "Embedding Model"

    Returns:
        vectors:"vector store"
    """    
    vector_store = FAISS.from_documents(chunks,embedding_model)
    return vector_store

def embedding_Pinecone(embedding_model,pinecone_api_key,environment,index_name,document):
    pinecone.init(
        api_key=pinecone_api_key,
        environment=environment
    )
    index_name=index_name
    
    vector_store=Pinecone.from_documents(document,embedding_model,index_name=index_name)
    return vector_store


# ## Search answers from VectorDB
# def retrieve_answers(query):
#     doc_search=retrieve_query(query)
#     print(doc_search)
#     response=chain.run(input_documents=doc_search,question=query)
#     return response




