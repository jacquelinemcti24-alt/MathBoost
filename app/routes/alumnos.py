from fastapi import APIRouter, Query, Path
from uuid import UUID
from app.models.alumnos import AlumnoCreate, AlumnoUpdate, AlumnoOut, AlumnoListOut, OneAlumnoOut
from app.service.alumnos_service import list_alumno, get_alumno, create_alumno, update_alumno, delete_alumno

router = APIRouter(prefix = "/alumnos",  tags=["Alumnos"])

@router.get("/", name= "listar_alumnos")
def inicio(
    limit:int=Query(100, ge=1, le=200), #Numero de registros a mostrar
    offset:int = Query(0, ge=0) #Desde que registro se va a mostar
):
    return list_alumno(limit, offset)

#Lista un producto
@router.get("/{alumnos_id}", response_model=OneAlumnoOut, name="obtener_alumnos")
def get_alumnos(alumnos_id:UUID):
    return get_alumno(alumnos_id)

#Insertar producto
@router.post("/", response_model=OneAlumnoOut, name="crear_alumnos")
def create_alumnos(body:AlumnoCreate):
    return create_alumno(body.model_dump())

#Actualizar producto
@router.put("/{alumnos_id}", response_model=OneAlumnoOut, name="actualizar_alumnos")
def update_alumnos(alumnos_id:UUID, body:AlumnoUpdate):
    return update_alumno(alumnos_id, body.model_dump())

#Eliminar producto
@router.delete("/{alumnos_id}", name="eliminar_alumnos")
def delete_alumnos(alumnos_id:UUID):
    return delete_alumno(alumnos_id)
