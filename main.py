import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(TG_TOKEN)

from src.utils.functions import chat_is_group, chat_is_private


def main():
    # TODO: add logic to get connection with api
    print("Bot started")


@bot.message_handler(commands=["start", "help"])
def send_welcome(message: telebot.types.Message):
    bot.reply_to(message, "Hello! I'm a bot that will help you manage your waifu list")


@bot.message_handler(func=lambda message: True)
def echo(message: telebot.types.Message):
    # TODO: add logic get chat type and increment message count if group or supergroup
    if chat_is_group(message):
        # TODO: increment message count if group in database
        print("increment message count")
        return
    print("new message on bot (this message is edited)")
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    main()
    bot.polling(none_stop=True)
