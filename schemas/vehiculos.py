def user1Entity(item) -> dict:
	return{
        "codvehiculo": item["codvehiculo"],
        "marca": item["marca"],
        "modelo": item["modelo"],
        "servicio": item["servicio"],
    	"color": item["color"],
    	"cilindraje": item["cilindraje"],
    	"estado": item["estado"],
    	"stock": item["stock"],
    	"categoria": item["categoria"],
        "precio": item["precio"],
    	"observaciones": item["observaciones"],
	}
def users1Entity(entity) -> list:
    	[user1Entity(item) for item in entity]
