from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import redirect_buttons
from utils import register_chat

from loader import dp


async def started_message(message: Message):
    """
    Start command text,
    it is received by the user
    when he first writes to the bot
    """
    await message.edit_text(
            text=(
                "Hi, I am a bot, able to send "
                "you <b>any photo by the selected category.</b>\n"
                "\n"
                "• <b>Simply select a category</b> and plot and bot "
                "will <b>send you a photo based on your choice.</b>\n"
                "\n"
                "• <b>You can also add me to your chats</b>, and "
                "participants will be able to browse photos.\n"
            ),
        reply_markup=redirect_buttons()
    )


@dp.message_handler(CommandStart())
async def send_welcome(message: Message):
    """
    /start command handler 
    :param message: Telegram message with "/start" command
    """
    a = await message.reply("woop")
    # Sending a start message
    await started_message(a)
    # Add chat to the database
    await register_chat(message)


@dp.callback_query_handler(text="start")
async def call_started_message(call: CallbackQuery):
    """
    Start calback handler
    """
    await call.answer()
    # Sending a start message
    await started_message(call.message)