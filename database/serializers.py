def retrieve_post_serial(todo):
    data = {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "publish": todo["publish"],
    }

    if todo.get("image"):
        data.update({"image": todo.get("image")})
    return data


def list_serial(todos):
    return [retrieve_post_serial(todo) for todo in todos]


def retrieve_user_serial(user):
    data = {"id": str(user["_id"]), "email": user["email"]}
    return data


def list_of_user_serial(users):
    return [retrieve_user_serial(user) for user in users]
