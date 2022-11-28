#from pymongo import MongoClient
#conexion = MongoClient()

import motor.motor_asyncio

from models.clientes import Clientes
MONGO_URL = 'mongodb+srv://jeison:Jeison2022@cluster0.jj0wxoy.mongodb.net/test'
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
conexion = Clientes.Concesionariodb

