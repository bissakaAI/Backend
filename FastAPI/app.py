from fastapi import FastAPI
from pydantic import BaseModel,Field
from dotenv import load_dotenv
import os
import uvicorn
from typing import Optional

load_dotenv()
data=[{"name": "Sam larry","age":20, "track":"Ai Developer"},{"name": "Sam","age":24,"track":"Ai"},
      {"name": "Sam larr","age":22,"track":"Ai Develop"}]

app = FastAPI(title='Simple FastAPI App',version='1.0.0')

#decorate the root function
@app.get("/") #endpoint is the root which is the forward slash
def root():
    return {'Message':'Welcome to my FastAPI Application'}


@app.get("/get-data")
def get_data():
    return data

#for a post request data is being sent from client to server so we need to define the type of data the client is allowed to send so that they wont pass rubbish information to us using pydantic 
 
#first we need to define the class
class Item(BaseModel):
    name: str = Field(...,example="Hamid")
    age: int =Field(...,example=25)
    track: str =Field(...,example="Fullstack Developer")

# Now lets create a post function
@app.post("/post-data")
def create_data(anyname:Item):
    data.append(anyname.dict())
    print(data)
    return {"message": "Data Received", "Data": data}


#now lets do an edith or patch 
# for patch we need to allow the other fields to be optional so we create a new class 

@app.put("/update-data/{id}") #{id}  is a path paraam
def update_data(id: int, req: Item):
    data[id].update(req.model_dump())
    print(data)
    return {"message": "Data updated", "Data": data}

# Implement an API endpoint to delete (REMOVE) a specific field from the DATA variable.
@app.delete("/remove-data/{id}")
def remove_data(id:int,req:Item):
    req=req.model_dump()
    dt=data[id]
    if (req["name"]==dt["name"]) & (req["age"]==dt["age"]):
        data.pop(id)
        print(data)
        return {"message": "Data updated", "Data": data}
    else:
        return {"message": "Data not found"}



# Implement an API endpoint to update (PATCH) a specific value in the DATA variable.
#since it is a patch request i need to have the id of the existing post i want to patch 
class ITEMO(BaseModel):
    name: Optional[str] = Field(None,example="Hamid")
    age: Optional[int] =Field(None,example=25)
    track: Optional[str] =Field(None,example="Fullstack Developer")

@app.patch("/modify-data/{id}")
def modify_data(id:int,req:ITEMO):
    data[id].update(req.model_dump(exclude_unset=True))
    print(data)
    return {"message": "Data successfuly modified", "Data": data}




if __name__ == '__main__':
    print(os.getenv('host'))
    print(os.getenv('port'))
    uvicorn.run(app,host=os.getenv("host"),port=int(os.getenv("port")))