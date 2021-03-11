from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def animals_categories():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="🦊 Fox", callback_data="fox")
    )
    markup.add(
        InlineKeyboardButton(text="🐈 Cat", callback_data="cat"),
        InlineKeyboardButton(text="🐕 Dog", callback_data="dog"),
    )
    markup.add(
        InlineKeyboardButton(text="🐼 Panda", callback_data="panda"),
        InlineKeyboardButton(text="👹 Red Panda", callback_data="red_panda"),
    )
    markup.add(
        InlineKeyboardButton(text="🦆 Duck", callback_data="duck"),
        InlineKeyboardButton(text="🦉 Owl", callback_data="owl")
    )
    markup.add(
        InlineKeyboardButton(text="🦎 Lizard", callback_data="lizard"),
        InlineKeyboardButton(text="🐨 Koala", callback_data="koala")
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data="menu")
    )

    return markup