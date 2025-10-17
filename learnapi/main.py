from fastapi import FastAPI
from fastapi.params import Body
from  pydantic import BaseModel

app =FastAPI()

class Post(BaseModel):
    name: str
    state: str

    
@app.get("/") # sets tthe endpoint
async def root():
    return {"message": "Hello world!!!thhfsbgs!"} # the response message

#this is a post request
@app.post("/posts")
def new_posts(payload:Post): # do post function to extract the body from the request and saving it in a dic
    print(payload.name)
    return {'newdata':f' the {payload} man'}
