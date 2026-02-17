from fastapi import FastAPI 
from app.routes import alumnos, cursos, maestros
from fastapi.exceptions import RequestValidationError
from app.core.exception import validation_exception_handler
from starlette.types import ExceptionHandler
from typing import cast

app = FastAPI()

# Manejo de errores 
#Requistro de exceptions
app.add_exception_handler(RequestValidationError, cast(ExceptionHandler, validation_exception_handler))

# Registrarb las rutas
app.include_router(alumnos.router)
app.include_router(cursos.router)
app.include_router(maestros.router)