import streamlit as st 
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)



if 'url' not in st.session_state:
    st.session_state.url = ''

if 'question' not in st.session_state:
    st.session_state.question=''


with st.form("from_1"):
    st.header("Ask Question To YouTube Video")
    st.session_state.url=st.text_input("Enter YouTube Video URL here :")
    st.session_state.question=st.text_input("Ask Question :")
    submit=st.form_submit_button("Submit")
    
    if submit:
        try :
            prompt=PromptTemplate(
            template="Answer the following question \n {question} from the following YouTube Video URl {text} ",
            input_variables=['question','text']
            )
                    
            parser=StrOutputParser()
            
            loader = YoutubeLoader.from_youtube_url(st.session_state.url)
            documents = loader.load()
            
            chain = prompt | model | parser
            
            result=chain.invoke({'question':st.session_state.question,'text':documents[0].page_content})
            
            st.write(result)
            
        except Exception as e:
            st.error(e)
            
