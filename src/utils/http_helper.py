import os
from dotenv import load_dotenv
import requests

from src.utils.functions import debug_message

load_dotenv()
base_url: str = os.getenv("API_BASE_URL")


def _handle_response(response: requests.Response) -> dict:
    print(response)
    if response.status_code >= 200 and response.status_code < 300:
        json_response = response.json()
        debug_message({"message": json_response, "level": "success"})
        return {
            "status": "success",
            "message": json_response["message"],
            "data": json_response["data"],
        }
    elif response.status_code == 404:
        debug_message({"message": "Profile not found", "level": "warning"})
        return {"status": "warning", "message": "Profile not found"}
    else:
        debug_message({"message": "Error on get user profile", "level": "error"})
        return {
            "status": "error",
            "message": "Error on get user profile",
        }


def get(url: str, params: dict = None, headers: dict = None, timeout: int = 30) -> dict:
    final_url = base_url + url
    debug_message({"message": f"fetch type get from {final_url}", "level": "comment"})
    request_method = requests.get
    result = request_method(
        final_url, params=params, headers=headers, timeout=timeout, verify=False
    )
    return _handle_response(result)


def post(url: str, data: dict = None, headers: dict = None, timeout: int = 30) -> dict:
    final_url = base_url + url
    debug_message({"message": f"fetch type post from {final_url}", "level": "comment"})
    request_method = requests.post
    result = request_method(
        final_url, data=data, headers=headers, timeout=timeout, verify=False
    )
    return _handle_response(result)
