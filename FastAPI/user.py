# in the py file we want to do stuffs to the user table  that has been created in the database

from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotenv
import uvicorn
# import bcrypt


load_dotenv()
app = FastAPI(title ="Simple User Interface",version ="1.0.0")

class Users(BaseModel):
    name: str =Field(...,example= "Adewale124 (with or without the numbers)")
    email: str =Field(...,example= "adewale@gmail.com")
    password: str =Field(...,pattern=r'^[A-Za-z0-9@_]+$')
# i want to create a signup endpoint 
# since users will be signing up te end point only needs to post 
@app.post("/signup") # a signup field wil be needing something to validate inputs so i create a class/model for that
def signup(input:Users):
    # duplicate_query = text("""SELECT * FROM users WHERE email= :email""")
    # db.execute(duplicate_query,{"email":input.email}).fetchone()
    try:
        query = text("""
                    INSERT INTO users(name,email,password) VALUES(:name,:email,:password)
                    """)
        db.execute(query,{"name":input.name,"email":input.email,"password":input.password})
        db.commit()
        return {"message":"user created successfully","Data":{"name":input.name,"email":input.email}}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
#login uses post too
class loginrequest(BaseModel):
    email: str
    password:str

@app.post("/login")
def login(input:loginrequest):
    try:
        query=text(""" SELECT * FROM users WHERE email= :email""")
        result=db.execute(query,{"email":input.email}).fetchone()
        print(result)
        # authentication
        if not result:
            raise HTTPException(status_code=401,detail="invalid email or password")
        verified_password= result[3]
        if input.email != verified_password:
            raise HTTPException(status_code=401,detail="invalid email or password")
        return {"message":"login sucessful"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
# for uthorization we would be needing a jwt so we will be installing pyJWT
# we also want anything that deals with token creation to be in a seperate
# for token generation we will need a secret key user details and expiration
# so i want to alter the initial table and add something to signify each users privilledge
# so to alter the table .. i cant go and be telling the devop guys that i want to insert a new column or delete...
# so alembic allows me that dynamics of altering the structure of my database 

    
if __name__ == '__main__':
    uvicorn.run(app,host=os.getenv("host"),port=int(os.getenv("port")))
    

