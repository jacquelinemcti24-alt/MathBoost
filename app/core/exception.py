from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


#MULTIPLICAR1 PATH
MENSAJES_ERROR = {
    "multiplicar_1_10":{ #Corresponde al name de la funcion
        "num1":{
            #greater_than_equal este error viene de la repuesta (type) que aparece en el navegador
            #cuando mandamos el priemr paramtri en el primer valor menor a 1
            "greater_than_equal":"El primer valor no puede ser menor a 1",
            "less_than_equal":"El primer numero no puede ser mayor a 10",
            "int_parsing":"El primer valor debe de ser un numero entero",
            "missing":"El primer campo dede ser obligatorio"
        },
        "num2":{
            "greater_than_equal":"El segundo valor no puede ser menor a 1",
            "less_than_equal":"El segundo numero no puede ser mayor a 10",
            "int_parsing":"El segundo valor debe de ser un numero entero",
            "missing":"El segundo campo dede ser obligatorio"
        }
    }
}

#Edta funcion se ejecuta en automatico cuando ocurre nun error
async def validation_exception_handler(request:Request,exc:RequestValidationError):
    errores = []
    route_obj = request.scope.get("route") #Que endPoint (ruta) es el que fallo
    ruta = getattr(route_obj, "name", "")
    #print (ruta)
    #print(exc.errors())
    for error in exc.errors():
        campo = error["loc"][-1] #Ultima posicion que se encuentra en el primer campo que fallo
        tipo = error["type"] #Tipo de error que ocurrio
        ruta_dicc = MENSAJES_ERROR.get(ruta,{})
        campo_dicc = ruta_dicc.get(campo,{})
        mensaje = campo_dicc.get(tipo)
        #Si hubo un mensaje lo recuperamos si no damos un mensaje por default
        errores.append(mensaje or f"Error en el campo '{campo}'")

        return JSONResponse( #Se prepara el mensaje final
            status_code = 422,
            content = {
                "error": "Datos invalidos",
                "detalles": errores
            }
        )