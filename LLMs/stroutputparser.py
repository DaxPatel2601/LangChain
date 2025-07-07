
# string parser 

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

# template 1
template_1=PromptTemplate(
    template="hello,write a detail report on {topic}",
    input_variables=['topic']
)

# template 2
template_2=PromptTemplate(
    template="hello,write a 5 line summary on {text}",
    input_variables=['text']
)

# parser 

parser=StrOutputParser()

# chaining 

chain = template_1 | model | parser | template_2 | model | parser 

result=chain.invoke({'topic':'black hole'})

print(result)
