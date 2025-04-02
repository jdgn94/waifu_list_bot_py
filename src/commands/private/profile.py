from src.utils.http_helper import get, post


def get_profile(id: int, username: str, name: str):
    response = get(f"/profiles/{id}")
    if response["status"] == "success":
        return response["data"]
    elif response["status"] == "warning":
        response = post(
            "/profiles", {"telegram_id": id, "username": username, "name": name}
        )
        print(response)
        if response["status"] == "success":
            return response["data"]
    return None
