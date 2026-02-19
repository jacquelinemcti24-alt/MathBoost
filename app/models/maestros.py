from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from uuid import UUID

class MaestroCreate(BaseModel):
    nombre:str = Field(min_length=1, max_length=200)
    email:str = Field(min_length=8, max_length=200)
    especialidad:str = Field(ge=0)
    #Revisar el Field
    
class MaestroUpdate(BaseModel):
    nombre:str | None = Field(min_length=1, max_length=200)
    email:str | None = Field(min_length=8, max_length=200)
    especialidad:str | None = Field(ge=0)
    
class MaestroOut(BaseModel):
    id: UUID
    nombre:str
    especialidad:str
    email:str
    telefono:str
    created_at:datetime
    update_at:datetime

class MaestroListOut(BaseModel):
    total:int
    items:list[MaestroOut]

class OneMaestroOut(BaseModel):
    item:MaestroOut
