from src.utils.http_helper import get, post


def get_profile(id: int, username: str | None, name: str | None):
    print("get profile function")
    try:
        response = get(f"/profiles/{id}")
        if response["status"] == "success":
            return response["data"]
        elif (
            response["status"] == "warning"
            and username is not None
            and name is not None
        ):
            response = post(
                "/profiles", {"telegram_id": id, "username": username, "name": name}
            )
            print(response)
            if response["status"] == "success":
                return response["data"]
        return None
    except Exception as e:
        print(e)
        return None
