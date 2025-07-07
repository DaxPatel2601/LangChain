from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template = """
    You are an intelligent information extractor.

    Given a formal personal introduction, extract the following information:

    Fields to extract:
    - name
    - experience
    - education
    - company_name
    - skills
    - college_name
    - batch
    - projects

    If any field is not mentioned, set its value to `null`.

    Formal Introduction:
  
    Expected Output (in JSON dictionary format):
    {
    "name": ...,
    "experience": ...,
    "education": ...,
    "company_name": ...,
    "skills": [...],
    "college_name": ...,
    "batch": ...,
    "projects": [...]
    }

"""
)

template.save('project/template.json')