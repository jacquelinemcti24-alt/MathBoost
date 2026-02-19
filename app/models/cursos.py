from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from uuid import UUID

class CursosCreate(BaseModel):
    nombre:str = Field(min_length=1, max_length=200)
    descripcion:str = Field(min_length=8, max_length=200)
    maestro_id:UUID = Field(ge=0)
    #Revisar el Field
    
class CursosUpdate(BaseModel):
    nombre:str | None = Field(min_length=1, max_length=200)
    descripcion:str | None = Field(min_length=8, max_length=200)
    maestro_id:UUID | None = Field(ge=0)
    
class CursosOut(BaseModel):
    id_cur: UUID
    nombre:str
    descripcion:str
    maestro_id:UUID
    created_at:datetime
    update_at:datetime

class CursosListOut(BaseModel):
    total:int
    items:list[CursosOut]

class OneCursosOut(BaseModel):
    item:CursosOut
