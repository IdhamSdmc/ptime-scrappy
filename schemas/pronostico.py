def pronosticoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "lugar": item["lugar"],
        "fecha": item["fecha"],
        "max": item["max"],
        "min": item["min"],
        "descripcion": item["descripcion"]
    }


def pronosticosEntity(entity) -> list:
    return [pronosticoEntity(item) for item in entity]
