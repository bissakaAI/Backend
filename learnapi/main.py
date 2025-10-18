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

#

# this is a code for delete using httpexceptions
# @app.delete("/delete/{id}")
# def delete_item(id: int, req: Item):
#     if id >= len(data):
#         raise HTTPException(status_code=404, detail="Item not found")

#     item = data[id]
#     for field, value in req.model_dump(exclude_unset=True).items():
#         if item.get(field) != value:
#             raise HTTPException(status_code=403, detail=f"{field} does not match")

#     deleted_item = data.pop(id)
#     return {"message": "Deleted successfully", "deleted": deleted_item}
