from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='RAG\Document Loaders\ML Files',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.load()

# print(docs[12].page_content)

docs = loader.lazy_load()

for documents in docs:
    print(documents.metadata)
    