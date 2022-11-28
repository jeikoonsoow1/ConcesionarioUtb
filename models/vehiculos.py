from typing import Optional
from pydantic import BaseModel

class Vehiculos(BaseModel):
    codvehiculo: Optional [str]
    marca: str
    modelo: str
    servicio: str
    color: str
    cilindraje: str
    estado: str
    stock: int
    categoria: str
    precio: int
    observaciones: str
