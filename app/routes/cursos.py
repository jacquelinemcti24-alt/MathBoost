from fastapi import APIRouter, Query, Path
from uuid import UUID
from app.models.cursos import CursosCreate, CursosUpdate, CursosOut, CursosListOut, OneCursosOut
from app.service.cursos_service import list_curso, get_curso, create_curso, update_curso, delete_curso

router = APIRouter(prefix = "/cursos",  tags=["Cursos"])

@router.get("/", name= "listar_curso")
def inicio(
    limit:int=Query(100, ge=1, le=200), #Numero de registros a mostrar
    offset:int = Query(0, ge=0) #Desde que registro se va a mostar
):
    return list_curso(limit, offset)

#Lista un producto
@router.get("/{curso_id}", response_model=OneCursosOut, name="obtener_curso")
def get_cursos(curso_id:UUID):
    return get_curso(curso_id)

#Insertar producto
@router.post("/", response_model=OneCursosOut, name="crear_curso")
def create_cursos(body:CursosCreate):
    return create_curso(body.model_dump())

#Actualizar producto
@router.put("/{curso_id}", response_model=OneCursosOut, name="actualizar_curso")
def update_cursos(curso_id:UUID, body:CursosUpdate):
    return update_curso(curso_id, body.model_dump())

#Eliminar producto
@router.delete("/{curso_id}", name="eliminar_curso")
def delete_cursos(curso_id:UUID):
    return delete_curso(curso_id)
