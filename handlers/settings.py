from aiogram.dispatcher.filters import CommandSettings
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import CallbackQuery, Message

from loader import dp
from keyboards import (
    settings_buttons,
    nsfw_setting_buttons
)


async def callback_admin_filter(call: CallbackQuery):

    chat = call.message.chat
    user = call.from_user

    # If the message is sent to a group
    if chat.type in ["supergroup", "group"]:
        # Get user status in a group chat
        member = await chat.get_member(user.id)
        # If the user does not have administrator rights
        if not member.status in ["creator", "administrator"]:
            # Inform about the restriction
            await call.answer(
                text=(
                    "👮🏻‍♀️ To do this, you need "
                    "to have administrator rights."
                ),
                show_alert=True
            )
            raise CancelHandler()


async def settings_message(message: Message):
    """
    This is the function
    for sending a message with settings
    """
    await message.edit_text(
        text=(
            "<b>🛠 This is the settings section.</b>\n"
            "\n"
            "<i>• So far, there are not so many of them here, "
            "but they will be replenished over time, well, "
            "or until I get an idea what else to add.</i>"
        ),
        reply_markup=settings_buttons()
    )


@dp.message_handler(CommandSettings())
async def send_settings(message: Message):
    """
    /settings command handler 
    :param message: "/settings" command
    """
    a = await message.reply("woop")
    # Sending a start message
    await settings_message(a)



@dp.callback_query_handler(text="settings")
async def call_settings(call: CallbackQuery):
    """
    Settings callback handler
    """
    await call.answer()
    # Editing the message
    await settings_message(call.message)


@dp.callback_query_handler(text="nsfw_setting")
async def nsfw_content_setting(call):
    """
    Redirect to the settings
    of access to nsfw content.
    """

    message = call.message
    chat = call.message.chat

    if chat.type == "private":
        # Returning Callback's Answer
        return await call.answer(
            text=(
                "📬 This button only works in groups."
            ),
            show_alert=True,
        )

    if call.data == "nsfw_setting":
        # Returning Callback's Answer
        return await call.answer(
            text=(
                "⏳ This feature will be added in future updates. Maybe."
                ),
                show_alert=True,
            )

    # Validation filter
    await callback_admin_filter(call)

    # Editing the message
    await message.edit_text(
        text=(
            "<b>🔞 This is the NSFW restrictions section</b>\n"
            "\n"
            "<i>• Here you can choose who can enter the anime hentai category. "
            "The default is «Administrators only»</i>"
        ),
        reply_markup=nsfw_setting_buttons()
    )