from fastapi import APIRouter

vehiculos = APIRouter()

@vehiculos.get('/vehiculos')
def saludo():
    return "Esta es la pag de vehiculos"
