import datetime
from telebot import types
from src.utils.functions import (
    chat_is_group,
    chat_is_private,
    chat_not_supported,
    get_message,
    language_code,
    debug_message,
)
from src.utils.http_helper import get, post


def start(message: types.Message):
    if chat_not_supported(message):
        return {"status": "error", "message": "Chat type not supported"}
    if message.from_user.is_bot:
        return {
            "status": "error",
            "message": "Bots are not allowed to use this command",
        }
    chat: int = message.chat
    user: types.User = message.from_user
    chat_language: str = language_code(message)
    print(f"User: {user}")
    print(f"Chat: {chat}")
    chat = _create_chat(chat.id, chat.type, chat_language)
    if not chat:
        return {"status": "error", "message": "Chat not found"}
    if chat_is_private(message):
        print("Private chat detected")
        if user.username is None:
            return {"status": "error", "message": "Username is not set"}
        full_name = user.first_name + " " + str(user.last_name)
        profile = _create_profile(user.id, user.username, full_name)
        debug_message({"message": profile, "level": "info"})
        if not profile:
            return {"status": "error", "message": "Profile not found"}
        print(profile)
        return {"status": "success", "message": "Private chat detected"}
    print("Group chat detected")
    return {"status": "success", "message": "Group chat detected"}


def info(message: types.Message):
    print("getting user info")
    response = get(f"/profiles/{message.from_user.id}")
    if response["status"] != "success":
        return get_message("error_profile", language_code(message))
    profile = response["data"]["profile"]

    chat = get(f"/chats/{message.chat.id}")
    if chat["status"] != "success":
        return get_message("error_chat", language_code(message))
    chat = chat["data"]["chat"]

    debug_message({"message": f"profile: {profile}\nchat: {chat}", "level": "info"})

    language = chat["language"]
    more_info = f"ℹ️ {get_message("more_info", language)}"
    if chat_is_private(message):
        more_info = f"""⬆️ *{get_message("exp", language)}:* {profile["exp"]} \/ {profile["limit_exp"]}
🪙 *{get_message("coins", language)}:* {profile["coins"]}
💎 *{get_message("diamonds", language)}:* {profile["diamonds"]}
📄 *{get_message("favorite_pages", language)}:* {profile["favorite_pages"]}
📄 *{get_message("favorite_pages_purchased", language)}:* {profile["favorite_pages_purchased"]}"""

    created_at = datetime.datetime.fromisoformat(profile["created_at"])
    text = f"""
    {get_message("info", language)}

*@{message.from_user.username}*
*Telegram ID: {message.from_user.id}*
{get_message("register_date", language)}: {created_at.strftime("%Y-%m-%d").replace("-", "\-")}
{"------------------------------------------".replace("-", "\-")}
    
💪 *{get_message("level", language)}:* {profile["level"]}
{more_info}"""

    return text


def _create_chat(chat_id: int, chat_type: str, language: str):
    response = get(f"/chats/{chat_id}")
    if response["status"] == "success":
        return response["data"]
    response = post(
        "/chats",
        {"telegram_id": id, "type": type, language_code: language_code},
    )
    return response


def _create_profile(user_id: int, username: str, name: str):
    response = post(
        "/profiles",
        {"telegram_id": user_id, "username": username, "name": name},
    )
    return response
