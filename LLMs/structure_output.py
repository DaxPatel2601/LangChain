# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# from typing import TypedDict

# load_dotenv()

# # schema
# class Review(TypedDict):
#     summary: str
#     sentiment : str

# model=ChatGroq(model="llama-3.1-8b-instant",   tools=[Review],temperature=0)

# structure_model= model.with_structured_output(Review)

# result=structure_model.invoke("hello")
# print(result)

from langchain_groq import ChatGroq
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.output_parsers import JsonOutputKeyToolsParser
from dotenv import load_dotenv

load_dotenv()

class Review(BaseModel):
    reviewer: str
    rating: int
    comment: str

structure_model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    tools=[Review],  # Define the function
    tool_choice="auto"
)

chain = structure_model | JsonOutputFunctionsParser()

result = chain.invoke("John gave a 4 star rating and said the service was good but can be improved.")
print(result)
