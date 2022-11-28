from fastapi import APIRouter

facturas = APIRouter()

@facturas.get('/facturas')
def saludo():
    return "Esta es la pag de facturas"
