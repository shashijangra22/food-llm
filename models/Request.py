from pydantic import BaseModel


class Request(BaseModel):
    plan: str
    loc: str
    time: str
