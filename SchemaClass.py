from pydantic import BaseModel, validator
from CustomDataTypes import Titles

class Response_Schema(BaseModel):
    id: int
    title: Titles

    @validator("id")
    def validate_id_value(cls, v):
        if v > 3:
            raise ValueError("Id is too big")
        else:
            return v