from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    nickname = Column(String)

# class Student(Base):
#     __tablename__= "StudentsData"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     grade= Column(Integer)
#     subject= Column(String)
