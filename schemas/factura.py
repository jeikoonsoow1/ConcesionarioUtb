def facturaEntity(item) -> dict:
	return{
    	"id": str(item["_id"]),
    	"numFactura": item["numFactura"],
    	"id_cliente": item["id_cliente"],
    	"fecha": item["fecha"],
    	"email": item["email"],
    	"telefono": item["telefono"],
        "valor": item["valor"],
        "impuesto": item["impuesto"],
	}
def facturasEntity(entity) -> list:
    	return [facturaEntity(item) for item in entity]
