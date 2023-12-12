def retrieve_serial(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "complete": todo["complete"],
    }


def list_serial(todos):
    return [retrieve_serial(todo) for todo in todos]
