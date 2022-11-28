from fastapi import APIRouter

clientes = APIRouter()

@clientes.get('/clientes')
def saludo():
    return "Esta es la página de clientes"
   
   