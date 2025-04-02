from src.utils.http_helper import get, post


def get_chat(id: int, type: str | None, language_code: str | None) -> dict | None:
    response = get(f"/chats/{id}")
    print(id, type, language_code)
    print(response)
    if response["status"] == "success":
        return response["data"]
    elif (
        response["status"] == "warning"
        and type is not None
        and language_code is not None
    ):
        response = post(
            "/chats", {"telegram_id": id, "type": type, language_code: language_code}
        )
        if response["status"] == "success":
            return response["data"]
        else:
            return None
    return None
