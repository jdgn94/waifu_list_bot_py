from telebot import types
from src.commands.private.chat import get_chat
from src.commands.private.profile import get_profile
from src.utils.functions import (
    chat_is_group,
    chat_is_private,
    chat_not_supported,
    get_message,
    language_code,
    debug_message,
)
from src.utils.message import send_text


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
    chat = get_chat(chat.id, chat.type, chat_language)
    if not chat:
        return {"status": "error", "message": "Chat not found"}
    if chat_is_private(message):
        print("Private chat detected")
        if user.username is None:
            return {"status": "error", "message": "Username is not set"}
        full_name = user.first_name + " " + str(user.last_name)
        profile = get_profile(user.id, user.username, full_name)
        debug_message({"message": profile, "level": "info"})
        if not profile:
            return {"status": "error", "message": "Profile not found"}
        print(profile)
        return {"status": "success", "message": "Private chat detected"}
    elif chat_is_group(message):
        print("Group chat detected")
        return {"status": "success", "message": "Group chat detected"}
    else:
        print("chat type not supported")
        return {"status": "error", "message": "Chat type not supported"}


def info(message: types.Message):
    print("getting user info")
    profile = get_profile(message.from_user.id)
    if not profile:
        return "Profile not found"

    chat = get_chat(message.chat.id)
    if not chat:
        return "Chat not found"

    debug_message({"message": f"profile: {profile}\nchat: {chat}", "level": "info"})

    language_code = chat.language
    more_info = f"ℹ️ {get_message("more_info", language_code)}"
    if chat_is_private(message):
        more_info = f"""
            
        ⬆️ {get_message("exp", language_code)}: {profile.exp} / {profile.limit_exp}
        🪙 {get_message("coins", language_code)}: {profile.coins}
        💎 {get_message("diamonds", language_code)}: {profile.diamonds}
        📄 {get_message("favorite_pages", language_code)}: {profile.favorite_pages}
        📄 {get_message("favorite_pages_purchased", language_code)}: {profile.favorite_pages_purchased}
        """

    text = f"""
    {get_message("info", language_code)}
    
    {message.from_user.username}
    Telegram ID: {message.from_user.id}
    
    ------------------------------------------
    
    💪 {get_message("level", language_code)}: {profile.level}
    {more_info}
    """

    return text
