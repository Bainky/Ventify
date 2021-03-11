from aiogram.types import BotCommand


async def on_startup_commands(dp):
    """
    Configuring commands for the bot at the first start.
    You can add the required commands here yourself.
    """
    await dp.bot.set_my_commands([
        BotCommand("start", "About me."),
        BotCommand("settings", "My settings.")
    ])
