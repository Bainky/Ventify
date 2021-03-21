# я писал этот код когда бухал так что говнокод - норма, а переписывать мне впадлу, не обессудь

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

import json


class LoggingMiddleware(BaseMiddleware):
    """
    Function for logging actions.
    It is needed to detect errors in the bot,
    otherwise how can you find out what caused the error?
    """
    async def on_process_message(self, message: Message, data: dict):

        parsed = json.loads(
            str(
                message
            )
        )
        res = json.dumps(
            parsed,
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )

        print(res)

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):

        parsed = json.loads(
            str(
                call
            )
        )
        res = json.dumps(
            parsed,
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )

        print(res)
