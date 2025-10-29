# in the py file we want to do stuffs to the user table  that has been created in the database

from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import text
import os
from dotenv import load_dotenv
from middleware import create_token
import uvicorn
# import bcrypt



load_dotenv()
token_time = int(os.getenv("token_time"))
app = FastAPI(title ="Simple User Interface",version ="1.0.0")

class Users(BaseModel):
    name: str =Field(...,example= "Adewale124 (with or without the numbers)")
    email: str =Field(...,example= "adewale@gmail.com")
    password: str =Field(...,pattern=r'^[A-Za-z0-9@_]+$')
    userType: Optional[str] =Field(...,example= "student")
# i want to create a signup endpoint 
# since users will be signing up the end point only needs to post 
@app.post("/signup") # a signup field wil be needing something to validate inputs so i create a class/model for that
def signup(input:Users):
    # duplicate_query = text("""SELECT * FROM users WHERE email= :email""")
    # db.execute(duplicate_query,{"email":input.email}).fetchone()
    try:
        query = text("""
                    INSERT INTO users(name,email,password,userType) VALUES(:name,:email,:password,:userType)
                    """)
        db.execute(query,{"name":input.name,"email":input.email,"password":input.password,"userType":input.userType})
        db.commit()
        return {"message":"user created successfully","Data":{"your name is name":input.name,"\nyor email is email":input.email}}
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
        result=db.execute(query,{"email":input.email}).fetchall()
        print(result)
        # authentication
        if not result:
            raise HTTPException(status_code=401,detail="invalid email or password")
        verified_password= result[3]
        if input.password != verified_password:
            raise HTTPException(status_code=401,detail="invalid email or password")
        
        create_token({
            "email":input.email,
            "userType":result.userType
            "id":result.id
        },token_time)
        return {"message":"login sucessful"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

# to add courses
class courses(BaseModel):
    title: str = Field(...,examples='chm101')
    level: int = Field(...,examples=400)
    
@app.post("/add-course")
def adcourses(input:courses):
    try:
        query = ("""INSERT INTO courses (title,level) VALUES(:title,:level)""")

        result=db.execute(query,{'title':input.title,'level':input.level})
        db.commit
        return {'message': result}
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
    


