from pydantic import BaseModel, ValidationError
from datetime import date
from typing import Optional, List


class User(BaseModel):
    id:int
    name:str
    # date|None = Optional[date]
    date_joined: Optional[date]
    department:List[str]

try:
    user = User(
        id="wacwc",
        name="zhangsan",
        date_joined=date(2020, 1, 1),
        department=['技术部', "产品部"]
    )
except ValidationError as e:
    print(e.errors())

# print(user.model_dump())