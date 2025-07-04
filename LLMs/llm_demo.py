from langchain_groq import ChatGroq
from dotenv import load_dotenv

print(load_dotenv())

llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.6)


while True:
    try:
        query=input("User:")
        if query!="stop":
            temp_result=llm.invoke(query)
            print(temp_result.content)
            
        else:
            print("Exit")
            exit()
    except Exception as e:
        print(e)
