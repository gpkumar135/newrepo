# from fastapi import FastAPI, Depends
#
# app = FastAPI()
# @app.get("/test")
# def index():
#     return {"FirstAPI":"Welcome to FastAPI"}
# from fastapi import FastAPI,Path
# from pydantic import BaseModel
# from typing import Optional
# class Employee(BaseModel):
#     name : str
#     role : str
# app = FastAPI()
#
# employee = {
#     1 : {
#         "name" : "pkg",
#         "role" : "dev"
#     },
#     2:{
#         "name":"Abdullah",
#         "role":"tester"
#     }
# }
# @app.get("/basic")
# def test():
#     return{"Test":"manual input"}
#
# @app.get("/test/{employee_id}")
# def test(employee_id:int ):
#     if employee_id in employee:
#         return employee[employee_id]
#     return {"data":"not found"}
#
# @app.get ("/query/{employee_id}")
# def get_by_query(employee_id:int, name:str):
#     for employee_id in employee:
#         if employee[employee_id]["name"] == name:
#             return employee[employee_id]
#         return {"name":"not found"}
#     return {"data":"not found"}
#
# @app.post("/post/{employe_id}")
# def create(employe_id: int, employe: Employee):
#     if employe_id in employee:
#         return {"Employee": "ID already exsists"}
#     employee[employe_id] = employe
#     return employee[employe_id]
#
#
# @app.put("/update/{employe_id}")
# def update(employe_id: int, employe: Employee):
#     if employe_id not in employee:
#         return {"Employe": "NOt exsists"}
#     employee[employe_id] = employe
#     return employee[employe_id]
#
# @app.put("/updatea/{employe_id}")
# def updatename(employe_id: int,name: Optional[str] = None,role: Optional[str]=None):
#     if employe_id not in employee:
#         return {"Employe": "NOt exsists"}
#     if name:
#         Employee[employe_id]["name"]=name
#     if role:
#         Employee[employe_id]["role"] = role
#     return employee[employe_id]
#
#
# @app.delete("/delete/{employe_id}")
# def delete_employee(employe_id:int):
#     if employe_id not in employee:
#         return {"Error":"employee doesn't exists"}
#     del employee[employe_id]
#     return {"employee":"Deleted"}
#
#
# ################################# DATABASE ###############################################

import asyncio

async def test():
    print("hello")
    await asyncio.sleep(5)
    print("test")

async def run_test():
    await test()

asyncio.run(run_test())
