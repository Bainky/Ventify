from middlewares import LoggingMiddleware
from aiogram import Dispatcher


async def setup_middlewares(dp: Dispatcher):
    """
    Launching middleware on first start
    """
    dp.middleware.setup(LoggingMiddleware())
