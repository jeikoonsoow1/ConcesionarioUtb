from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Envios(BaseModel):
    id: Optional[str]
    idClientes: int
    valor_envio: int
    fecha_envio: datetime
    origen: str
    destino: str
    estado_de_envio: str
    transportadora: str
