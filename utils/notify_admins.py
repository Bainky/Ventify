from aiogram import Dispatcher
from data.config import BOT_OWNER


async def on_startup_notify(dp: Dispatcher):
    """
    This function notifies administrators that the bot is running.
    """
    await dp.bot.send_message(BOT_OWNER, "🟢")


async def on_shutdown_notify(dp: Dispatcher):
    """
    This feature notifies administrators that a bot has died.
    """
    await dp.bot.send_message(BOT_OWNER, "🔴")