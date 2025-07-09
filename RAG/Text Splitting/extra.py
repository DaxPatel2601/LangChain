import requests

data=requests.post("https://demo-k46b.onrender.com",data={"joke_id":1,'text':'hello'})
mydata=data.json()
print(mydata)
print(type(mydata))

