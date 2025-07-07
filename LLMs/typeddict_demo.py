#structure output 

# use case 

# 1 Data extraction 
 # for example : upload a resume , extract text from it and convert that data into jason formate and after store that data into database itself 
 
# 2 API build 
 # amazon -- > review --> topic,pros,cons,sentiment analysis , build API and forward this info using API 
 
# 3 Agents 
  # tools 

# LLM --> auto structure output AND un structure 

# typed dictionary 
# pydantic 
# jason_structure 

from typing import TypedDict

class Person(TypedDict):
    
    name:str
    age:int
    
new_person:Person ={'name':'dx','age':52}

print(new_person)