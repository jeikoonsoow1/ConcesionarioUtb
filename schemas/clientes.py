def userEntity(item) -> dict:
	return{
    	"id": str(item["_id"]),
    	"idClientes": item["idClientes"],
    	"nombre": item["nombre"],
        "direccion": item["dirección"],
    	"telefono": item["telefono"],
    	"email": item["email"]    	
	}
def usersEntity(entity) -> list:
    	return [userEntity(item) for item in entity]
 
 
