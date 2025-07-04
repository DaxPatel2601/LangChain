from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage


load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

chat_history = [
    SystemMessage(content='You are helpful AI assistant')
]

# simple chatbot


while True:
    user_input=input("user : ")
    if user_input=="stop":
        print("stop")
        break

    chat_history.append(HumanMessage(content=user_input))

    result=model.invoke(chat_history)

    chat_history.append(AIMessage(result.content))
    print(f"AI : {result.content}")
    

print(chat_history)
