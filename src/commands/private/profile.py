from src.utils.http_helper import get


def get_profile(id: int):
    print(id)
    response = get(f"/profiles/{id}")

    return response
