from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('E:\SoftQube\LangChain\RAG\Document Loaders\AI.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))



# | **Use Case**                   | **Recommended Loader**                               |
# | ------------------------------ | ---------------------------------------------------- |
# | Simple, clean PDFs             | `PyPDFLoader`                                        |
# | PDFs with tables/columns       | `PDFPlumberLoader`                                   |
# | Scanned/image PDFs             | `UnstructuredPDFLoader` or `AmazonTextractPDFLoader` |
# | Need layout and image data     | `PyMuPDFLoader`                                      |
# | Want best structure extraction | `UnstructuredPDFLoader`                              |


# https://python.langchain.com/docs/integrations/document_loaders/



