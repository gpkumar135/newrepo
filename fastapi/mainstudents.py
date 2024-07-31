# from typing import Optional
# from models import Base, Student
# from pydantic import BaseModel
# from schema import StudentSchema
# from database import engine1,Sessionlocal1
# from sqlalchemy.orm import Session
# from fastapi import FastAPI,Depends
#
# Base.metadata.create_all(bind=engine1)
# app=FastAPI()
#
# def get_db():
#     try:
#         db = Sessionlocal1()
#         yield db
#     finally:
#         db.close()
#
# @app.post("/student/post")
# def add_user(request:StudentSchema, db: Session = Depends(get_db)):
#     user = Student(id=request.id, name=request.name,  grade= request.grade,subject=request.subject)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
# @app.get("/Student/id")
# def get_users(id,db: Session= Depends(get_db)):
#     users = db.query(Student).filter(Student.id == id).first()
#     return users
