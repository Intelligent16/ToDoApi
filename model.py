from datetime import datetime

from pydantic import BaseModel


class Todo (BaseModel):
    id: int
    creationDate: datetime
    text: str
    description: str
