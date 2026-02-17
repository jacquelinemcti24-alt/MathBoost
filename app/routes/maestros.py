from fastapi import APIRouter, Query, Path
from uuid import UUID
from app.models.maestros import MaestroCreate, MaestroUpdate, MaestroOut, MaestroListOut, OneMaestroOut
from app.service.maestros_service import list_maestro, get_maestro, create_maestro, update_maestro, delete_maestro

router = APIRouter(prefix = "/maestros",  tags=["Maestros"])

@router.get("/", name= "listar_maestro")
def inicio(
    limit:int=Query(100, ge=1, le=200), #Numero de registros a mostrar
    offset:int = Query(0, ge=0) #Desde que registro se va a mostar
):
    return list_maestro(limit, offset)

#Lista un producto
@router.get("/{maestro_id}", response_model=OneMaestroOut, name="obtener_maestro")
def get_materias(maestro_id:UUID):
    return get_maestro(maestro_id)

#Insertar producto
@router.post("/", response_model=OneMaestroOut, name="crear_maestro")
def create_materias(body:MaestroCreate):
    return create_maestro(body.model_dump())

#Actualizar producto
@router.put("/{maestro_id}", response_model=OneMaestroOut, name="actualizar_maestro")
def update_materias(maestro_id:UUID, body:MaestroUpdate):
    return update_maestro(maestro_id, body.model_dump())

#Eliminar producto
@router.delete("/{maestro_id}", name="eliminar_maestro")
def delete_materias(maestro_id:UUID):
    return delete_maestro(maestro_id)
