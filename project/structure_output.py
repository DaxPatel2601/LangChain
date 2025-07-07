import streamlit as st 
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal
from typing import Optional
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import json


load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)
result_copy=None

# result={}

class intro(BaseModel):
    name: str = Field(description="a string representing full name of the employee")
    experience: str=Field(default=0,description="a string represent employee`s total year or month of experience")
    education: str=Field(default=None,description="a string represent employee`s higher education , don`t take collage name")
    company_name: str=Field(default=None,description="a string represent name of the employee`s last or current company name")
    skills: list[str]=Field(default=None,description="a list of string represent skills which is mentioned by employee")
    collage_name:str=Field(default=None,description="a string represent the name of the employee`s last collage name")
    batch:Optional[str]=Field(default=None,description="a string represent the employee`s pass out year")
    projects:Optional[list[str]]=Field(default=None,description="a list of string represent the name of the project which employee mentioned")

structured_model = model.with_structured_output(intro)

with st.form("from1"):
    st.header("Introduce Your Self")
    st.info("This project extract your data from formal introduction and convert into dictionary")
    user_input=st.text_input("Introduction:")
    submit=st.form_submit_button("Submit")
    
    if submit:
        template=load_prompt('template.json')
        chain = template | structured_model
        result=structured_model.invoke(user_input)
        result_copy=result.model_dump_json()
        st.write(result)

if result_copy is not None:
    # Create download button
    st.download_button(
        label="📥 Download Extracted Info as JSON",
        data=result_copy,
        file_name="extracted_info.json",
        mime="application/json"
    )