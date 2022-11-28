from fastapi import APIRouter

envios = APIRouter()

@envios.get('/envios')
def saludo():
    return "Esta es la página de envios"

 