from dotenv import load_dotenv
import streamlit as st 
from langchain_groq import ChatGroq


load_dotenv()

with st.form("form1"):
    uploaded_file=st.header("Upload Your Document")
    document=st.file_uploader("Upload Your Document Here:",type=['pdf','docs','docx','csv'])
    submit=st.form_submit_button("Submit")
    
    if submit:
        if uploaded_file is not None:
            file_name = uploaded_file.name
            file_extension = file_name.split(".")[-1].lower()
            st.write(file_extension)
            # st.download_button(
            #     label="📥 Download File",
            #     data=uploaded_file.getvalue(),
            #     file_name=uploaded_file.name,
            #     mime=uploaded_file.type
            # )
            
            # if file_type == "pdf":
            #    pass
            # elif file_type == "csv":
            #     pass
            # elif file_type == "docx" or file_type =="docs":
            #     pass
            # else:
            #     st.error("Unsupported file type")

    