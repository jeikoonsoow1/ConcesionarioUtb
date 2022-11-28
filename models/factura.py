from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Factura(BaseModel):
    numFactura: Optional[str]
    id_cliente: int
    fecha: datetime
    email: str
    telefono: int
    valor: int
    impuesto: int
