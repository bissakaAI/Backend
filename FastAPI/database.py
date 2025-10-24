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