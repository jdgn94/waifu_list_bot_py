import os
import telebot
from dotenv import load_dotenv
from src.commands.general.index import info, start
from src.utils.message import send_text
from src.utils.functions import chat_is_group, debug_message, chat_not_supported

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(TG_TOKEN)


def main():
    # TODO: add logic to get connection with api
    print("Bot started")


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: telebot.types.Message):
    response = start(message)
    send_text(bot, message.chat.id, response["message"])


@bot.message_handler(commands=["info"])
def user_info(message: telebot.types.Message):
    if chat_not_supported(message):
        return send_text(bot, message.chat.id, "This chat type is not supported")

    message = info(message)
    return send_text(bot, message.chat.id, message, reply_to_message_id=message.id)


@bot.message_handler(func=lambda message: True)
def echo(message: telebot.types.Message):
    # TODO: add logic get chat type and increment message count if group or supergroup
    if chat_is_group(message):
        # TODO: increment message count if group in database
        print("increment message count")
        return
    debug_message({"message": message, "level": "info"})
    send_text(
        bot, message.chat.id, "Echo: " + message.text, reply_to_message_id=message.id
    )


if __name__ == "__main__":
    main()
    bot.polling(none_stop=True)
