from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker                                                                                  
from dotenv import load_dotenv
import os
from pymysql.constants import CLIENT
load_dotenv()

db_url = f'mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}'
engine = create_engine(db_url,connect_args={"client_flag":CLIENT.MULTI_STATEMENTS})
# engine = create_engine(db_url)
session=sessionmaker(bind=engine)
db=session()

<<<<<<< HEAD
# query= text("SELECT * FROM user")
# userd=db.execute(query).fetchall()
# print(userd)
 
create_tables_query = text("""
CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                           email VARCHAR(100) NOT NULL,
                           password VARCHAR(20) NOT NULL);


CREATE TABLE IF NOT EXISTS courses(id INT AUTO_INCREMENT PRIMARY KEY,
                           title VARCHAR(100) NOT NULL,
                           level VARCHAR(100) NOT NULL);
                        
CREATE TABLE IF NOT EXISTS enrollments(id INT AUTO_INCREMENT PRIMARY KEY,
                           userid INT,
                           courseid INT,
                           FOREIGN KEY(userid) REFERENCES users(id),
                           FOREIGN KEY(courseid) REFERENCES courses(id));
""")

databseusercourses=db.execute(create_tables_query)
# i removed the fetchall() because the sql query doesnt have anything to return it is not a query that returns something so its going to throw an error 
print(databseusercourses)
=======
query= text("SELECT * FROM user")
userd=db.execute(query).fetchall()
print(userd)



create_tables_query =



# from database import db
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from sqlalchemy import text
# import os
# from dotenv import load_dotenv
# import bcrypt
# import uvicorn

# load_dotenv()

# app = FastAPI(title="Simple App", version="1.0.0")

# class Simple(BaseModel):
#     name: str = Field(..., example="Sam Larry")
#     email: str = Field(..., example="sam@email.com")
#     password: str = Field(..., example="sam123")

# @app.post("/signup")
# def signUp(input: Simple):
#     try:

#         duplicate_query=text("""
#             SELECT * FROM users
#             WHERE email = :email
#                              """)
#         existing = db.execute(duplicate_query, {"email": input.email})
#         if existing:
#             print("Email already exists")
#             # raise HTTPException(status_code=400, detail="Email already exists")


#         query = text("""
#             INSERT INTO users (name, email, password)
#             VALUES (:name, :email, :password)
#         """)

#         salt = bcrypt.gensalt()
#         hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)
#         print(hashedPassword)

#         db.execute(query, {"name": input.name, "email": input.email, "password": hashedPassword})
#         db.commit()

#         return {"message": "User created successfully",
#                 "data": {"name": input.name, "email": input.email}}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail = e)
    
# if __name__=="__main__":
#     uvicorn.run(app,host=os.getenv("host"), port=int(os.getenv("port")))
>>>>>>> 9074a65600479179af92be58e1de0128158a3753
