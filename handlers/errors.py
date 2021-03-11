from aiogram.utils.exceptions import MessageNotModified
from loader import dp


@dp.errors_handler(exception=MessageNotModified)
async def user_floods_callback_requests(update, exception):
    """
    This error occurs when the user simultaneously
    pressed the same inline button in a short time.
    """
    return True