import os
from telebot import TeleBot, types
from src.utils.http_helper import get


def send_text(
    bot: TeleBot,
    chat_id: int,
    text: str,
    reply_to_message_id: int = None,
    reply_markup: types.ReplyKeyboardMarkup = None,
    disable_web_page_preview: bool = False,
    timeout: int = None,
    **kwargs: dict
):
    bot.send_message(
        chat_id or bot.chat.id,
        text,
        reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup,
        disable_web_page_preview=disable_web_page_preview,
        timeout=timeout,
        parse_mode="MarkdownV2",
        **kwargs
    )
