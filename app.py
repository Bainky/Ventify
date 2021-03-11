from aiogram import executor

from handlers import dp
from utils import (
    setup_middlewares,
    on_startup_notify,
    on_startup_commands,
    on_shutdown_notify,
    on_shutdown_close_db
)


async def on_startup(dispatcher):
    """
    This function is activated when the bot starts.
    """
    await setup_middlewares(dispatcher)
    await on_startup_notify(dispatcher)
    await on_startup_commands(dispatcher)


async def on_shutdown(dispatcher):
    """
    This function is activated when the bot is shutdown.
    """
    await on_shutdown_close_db(dispatcher)
    await on_shutdown_notify(dispatcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)