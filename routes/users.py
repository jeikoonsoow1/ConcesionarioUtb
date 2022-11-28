from fastapi import APIRouter

usuarios = APIRouter()

@usuarios.get('/users')
def saludo():
    return "Bienvenido a mi pagina"

