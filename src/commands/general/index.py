from telebot import types
from src.commands.private.chat import get_chat
from src.commands.private.profile import get_profile
from src.utils.functions import (
    chat_is_group,
    chat_is_private,
    chat_not_supported,
    language_code,
    debug_message,
)


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
