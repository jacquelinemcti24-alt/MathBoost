from uuid import UUID
from datetime import datetime, timezone
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from app.core.supabase_client import get_supabase
from app.core.config import config
from postgrest import CountMethod

def _table():
    sb = get_supabase()
    return sb.schema(config.supabase_schema).table(config.table_curso)

#MOSTRAR PRODUCTOS
def list_curso(limit:int=100, offset:int=0):
    try:
        print("antes de Supabase:")
        res = _table().select("*", count=CountMethod.exact).range(offset, offset+limit-1).execute() 
        print(res)
        return {"items":res.data or [], "total": res.count or 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Curso no encontrado")
    
def get_curso(curso_id:UUID):
    try:
        res = _table(). select("*").eq("id", str(curso_id)).limit(1).execute()
        data = res.data or []
        return data[0]
    except Exception as e:
        raise HTTPException(status_code=404, detail="Curso no encontrado")

#CREAR UN CURSO
def create_curso(datos:dict):
    try: 
        if not datos: 
            raise HTTPException(status_code=404, detail="Campos no enviados, para registrar")
        datos  = jsonable_encoder(datos)
        res = _table().insert(datos).execute()
        return res.data[0] if res.data else None

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Falló al insertar el registro {str(e)}")

#ACTUALIZAR UN CURSO
def update_curso(curso_id:UUID, datos:dict):
    try:
        if not datos: 
            raise HTTPException(status_code=404, detail="Campos no enviados, patra registrar")
        datos = jsonable_encoder(datos)
        res =_table().update(datos).eq("id",str(curso_id)).execute()
        return res.data[0] if res.data else None
    
    except Exception as e:
        raise HTTPException(swtatus_code=404, detail="Curso no encontrado")

#BORRAR UN CURSO
def delete_curso(curso_id:UUID):
    try:
        res = _table().delete().eq("id", str(curso_id)).execute()
        return res.data[0] if res.data else None
    
    except Exception as e:
        raise HTTPException(swtatus_code=404, detail="Curso no encontrado")

