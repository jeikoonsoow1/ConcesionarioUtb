from typing import Optional
from pydantic import BaseModel

class Clientes(BaseModel):
    id: Optional[str]
    idClientes: int
    nombre: str
    direccion: str
    telefono: int
    email: str

