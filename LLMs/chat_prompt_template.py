from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage


chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} expert'),
    ('system','explain in simple terms ,what is {topic}')
])


prompt=chat_template.invoke({
    'domain':'cricket',
    'topic':"over"
})

print(prompt)