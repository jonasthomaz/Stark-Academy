from pydantic import BaseModel


class ResponseRequestModel(BaseModel):
    message: str
