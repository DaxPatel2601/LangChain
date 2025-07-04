from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import keyboard
import random
import time

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

chat_history = []

# simple chatbot


while True:
    user_input=input("user : ")
    if user_input=="stop":
        print("stop")
        break
    
    
    template = PromptTemplate(
        input_variables=["question"],
        template="""
    You are an expert AI that answers user queries.

    Rules:
    1. Be honest and accurate.
    2. Do not hallucinate.
    3. Do not answer if the question is illegal or unethical.
    4. Answer in one line only

    Question: {question}
    """
    )
    chat_history.append(user_input)

    chain = template | model
    result=chain.invoke({
        'question':chat_history
    })

    chat_history.append(result.content)
    print(f"AI : {result.content}")
    

print(chat_history)
    
    