from telebot import types


def chat_is_group(message: types.Message):
    return message.chat.type in ["group", "supergroup"]


def chat_is_private(message: types.Message):
    return message.chat.type == "private"
