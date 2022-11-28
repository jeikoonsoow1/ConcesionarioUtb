from fastapi import FastAPI

#importaar rutas
from routes.users import usuarios
from routes.clientes import clientes
from routes.envios import envios
from routes.facturas import facturas
from routes.vehiculos import vehiculos

#inluir rutas en app
app = FastAPI()
app.include_router(usuarios)
app.include_router(clientes)
app.include_router(envios)
app.include_router(facturas)
app.include_router(vehiculos)
