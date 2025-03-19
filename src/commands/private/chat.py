from src.utils.http_helper import get, post


def get_chat(id: int):
    print(id)
    response = get(f"/chats/{id}")
    print(response)
    if response["status"] == "success":
        return response["data"]
    elif response["status"] == "warning":
        response = post("/chats", {"id": id})
        if response["status"] == "success":
            return response["data"]
        else:
            return None
    return None
