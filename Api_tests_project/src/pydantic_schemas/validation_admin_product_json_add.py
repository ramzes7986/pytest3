from pydantic import BaseModel, constr, validator
from typing import List


class Base(BaseModel):
    id: int
    name: str
    guid: str
    description: str
    price: constr(regex='^300$') = '300'
    categoryIds: List[int]

    @validator("id")
    def check_that_id_is_equal_to_300704(cls, v):
        if id != 300704:
            raise ValueError("id is not 300704")
        else:
            return v




