from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

prompt_1= PromptTemplate(
    template='Generate a detail report on {topic} ',
    input_variables=['topic']
)

prompt_2= PromptTemplate(
    template='Generate a 5 pointer summary from following text \n {text}',
    input_variables=['text']
)

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser 
result= chain.invoke({'topic':'earth'})
print(result)

chain.get_graph().print_ascii()