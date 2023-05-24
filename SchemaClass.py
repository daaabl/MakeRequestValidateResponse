from pydantic import BaseModel, validator
from CustomDataTypes import Titles
from messages import Error_Messages

class Response_Schema(BaseModel):
    id: int
    title: Titles

    @validator("id")
    def validate_id_value(cls, v):
        if v > 2:
            raise ValueError(Error_Messages.BIG_ID)
        else:
            return v