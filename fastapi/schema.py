from pydantic import BaseModel

class UserSchema (BaseModel):
    id : int
    email : str
    nickname : str
    name : str


# class StudentSchema(BaseModel):
#     id:int
#     name:str
#     grade: int
#     subject : str

