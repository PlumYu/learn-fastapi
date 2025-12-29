# 模型
# 1.orm
# 2.pydantic

from pydantic import BaseModel
from typing import List

class UserSchema(BaseModel):
    id:int
    email:str
    username:str
    mobile:str

class UserListSchemaOut(BaseModel):
    users:List[UserSchema]
