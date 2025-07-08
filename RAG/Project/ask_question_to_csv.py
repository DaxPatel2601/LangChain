import streamlit as st 
from langchain_groq import ChatGroq
from langchain_community.document_loaders import CSVLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

with st.form("form1"):
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    question = st.text_input("Ask Question :")
    submit=st.form_submit_button("Submit")
    
    if submit:

        if uploaded_file is not None:
            
            df = pd.read_csv(uploaded_file)
            file_path="E:\SoftQube\LangChain\RAG\Project\csv_files\csv_file_1.csv"
            df.to_csv(file_path)
            
            prompt=PromptTemplate(
            template="Answer the following question \n {question} from the csv file text  {text} ",
            input_variables=['question','text']
            )
                    
            parser=StrOutputParser()
            
            loader = CSVLoader(file_path)
            documents = loader.load()
                        
            chain = prompt | model | parser
            
            result=chain.invoke({'question':question,'text':documents[0]})
            
            st.write(result)
                
