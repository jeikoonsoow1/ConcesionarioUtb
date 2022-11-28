def envioEntity(item) -> dict:
	return{
    	"id": str(item["_id"]),
    	"idClientes": item["idClientes"],
    	"valor_envio": item["valor_envio"],
        "fecha_envio": item["fecha_envio"],
        "origen": item["origen"],
        "destino": item["destino"],
        "estado_de_envio": item["estado_de_envio"],
        "trasportadora": item["trasportadora"], 
	}
	
def enviosEntity(entity) -> list:
    	return [envioEntity(item) for item in entity]
