# я писал этот код когда бухал так что говнокод - норма, а переписывать мне впадлу, не обессудь

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from logging import warning


class LoggingMiddleware(BaseMiddleware):
    """
    Function for logging actions.
    It is needed to detect errors in the bot,
    otherwise how can you find out what caused the error?
    """
    async def on_process_message(self, message: Message, data: dict):

        chat = message.chat
        user = message.from_user

        if message.chat.type == "private":
            warning(f"Command: [{message.text}] > [{user.full_name}]")

        if message.chat.type in ["group", "supergroup"]:
            warning(f"Command: [{message.text}] > [{chat.title}][ > [{user.full_name}]")

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):

        chat = call.message.chat
        user = call.from_user

        if chat.type == "private":
            warning(f"Callback: [{call.data}] > [{user.full_name}]")

        if chat.type in ["group", "supergroup"]:
            warning(f"Callback: [{call.data}] > [{chat.title}] > [{user.full_name}]")
