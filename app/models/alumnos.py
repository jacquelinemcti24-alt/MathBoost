from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from uuid import UUID

def validar_matricula(value: int) -> int:
    if len(str(value)) != 10:
        raise ValueError("La matrícula debe tener exactamente 10 dígitos")
    return value

class AlumnoCreate(BaseModel):
    nombre:str = Field(min_length=1, max_length=200)
    email:str = Field(min_length=8, max_length=200)
    matricula:int = Field(ge=0)
    #Revisar el Field
    @field_validator("matricula")
    @classmethod
    def validar_matricula(cls, value:int ) -> int:
        return validar_matricula(value)
    
class AlumnoUpdate(BaseModel):
    nombre:str | None = Field(min_length=1, max_length=200)
    email:str | None = Field(min_length=8, max_length=200)
    matricula: int | None = Field(gt=0) # gt=greater than
    
class AlumnoOut(BaseModel):
    id: UUID
    nombre:str
    email:str
    matricula:int
    carrera:str
    telefono:str
    created_at:datetime
    update_at:datetime

class AlumnoListOut(BaseModel):
    total:int
    items:list[AlumnoOut]

class OneAlumnoOut(BaseModel):
    item:AlumnoOut
