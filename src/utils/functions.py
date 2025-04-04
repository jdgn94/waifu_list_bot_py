from enum import Enum
from telebot import types
from termcolor import colored
from translations.index import messages


class LogLevel(Enum):
    DEBUG = "debug"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    COMMENT = "comment"


type LogMessage = dict["message":str, "level" : LogLevel | LogLevel("info")]


def debug_message(values: LogMessage | list[LogMessage]):
    def printMessage(value: LogMessage):
        level = value["level"]
        color = None
        background = None
        if level == "info":
            color = "blue"
        elif level == "success":
            color = "green"
        elif level == "debug":
            color = "magenta"
        elif level == "warning":
            color = "yellow"
        elif level == "error":
            color = "red"
        elif level == "critical":
            color = "white"
            background = "on_red"
        elif level == "comment":
            color = "dark_grey"

        text = colored(value["message"], color, background, ["bold"])
        print(text)

    if values is list:
        values.foreach(lambda x: printMessage(x))
    else:
        printMessage(values)


def chat_is_group(message: types.Message):
    return message.chat.type in ["group", "supergroup"]


def chat_is_private(message: types.Message):
    return message.chat.type == "private"


def chat_not_supported(message: types.Message):
    return message.chat.type not in ["private", "group", "supergroup"]


def language_code(message: types.Message):
    return message.from_user.language_code


def is_bot(message: types.Message):
    return message.from_user.is_bot


def get_message(key: str, language_code: str):
    return messages[key][language_code]
