from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import random
from langchain_core.prompts import PromptTemplate , load_prompt

load_dotenv()
model=ChatGroq(model="llama-3.1-8b-instant",temperature=0.5)

template=load_prompt('template.json')

with st.form("form1"):
    
    st.header("Research Paper")
    
    paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", 
        "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

    style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", 
        "Code-Oriented", "Mathematical"])

    length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", 
        "Medium (3-5 paragraphs)", "Long (detailed explanation)"])
    
    submit=st.form_submit_button("Submit")
    
    
if submit:
    chain = template | model
    result=chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)
        
    