
# string parser 

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

# parser 

parser=JsonOutputParser()


# template 1
template_1=PromptTemplate(
    template="give me name of the cities of gujarat state {formate_instruction}",
    input_variables=[],
    partial_variables={'formate_instruction':parser.get_format_instructions()}
)

chain = template_1 | model | parser

result=chain.invoke({})

print(result)

# we dont apply schema to json or we cannot manually set schema 
 