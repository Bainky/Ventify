from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def control_buttons(back_data):

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="⚡️ Generate!", callback_data="generate_new")
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data=back_data)
    )

    return markup