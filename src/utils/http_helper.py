import os
from dotenv import load_dotenv
import requests

load_dotenv()
base_url: str = os.getenv("API_BASE_URL")


def _handle_response(response: requests.Response) -> dict:
    if response.status_code >= 200 and response.status_code < 300:
        return {"status": "success", "data": response.json()}
    elif response.status_code == 404:
        return {"status": "warning", "message": "Profile not found"}
    else:
        return {
            "status": "error",
            "message": "Error on get user profile",
        }


def get(url: str, params: dict = None, headers: dict = None, timeout: int = 30) -> dict:
    final_url = base_url + url
    print(final_url)
    request_method = requests.get
    result = request_method(
        final_url, params=params, headers=headers, timeout=timeout, verify=False
    )
    return _handle_response(result)


def post(url: str, data: dict = None, headers: dict = None, timeout: int = 30) -> dict:
    final_url = base_url + url
    print(final_url)
    request_method = requests.post
    result = request_method(
        final_url, data=data, headers=headers, timeout=timeout, verify=False
    )
    return _handle_response(result)
