from pydantic import BaseModel

class MaterialCreate(BaseModel):
    text: str

