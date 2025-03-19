from telebot import types
from src.commands.private.chat import get_chat
from src.commands.private.profile import get_profile
from src.utils.functions import chat_is_group, chat_is_private


def start(message: types.Message):
    if chat_is_private(message):
        print("Private chat detected")
        chat_id = message.chat.id
        user_id = message.from_user.id
        print(chat_id)
        chat = get_chat(chat_id)
        if not chat:
            return {"status": "error", "message": "Chat not found"}
        profile = get_profile(user_id)
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
