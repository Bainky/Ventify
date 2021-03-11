from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import BOT_USER

def menu_with_categories():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="🎉 Anime", callback_data="anime"),
        InlineKeyboardButton(text="🐉 Animals", callback_data="animals")
    )
    markup.add(
        InlineKeyboardButton(text="🤡 Memes", callback_data="memes")
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data="start")
    )

    return markup 


def redirect_buttons():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="🚀 Categories", callback_data="menu"),
        InlineKeyboardButton(text="⚙️ Settings", callback_data="settings")
    )
    markup.add(
        InlineKeyboardButton(text="🧷 Add a bot to your chat", url=f"t.me/{BOT_USER}?startgroup=true")
    )
    markup.add(
        InlineKeyboardButton(text="📝 Source Code", url="github.com/Bainky/Ventify")
    )

    return markup


def settings_buttons():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="🔐 NSFW Content", callback_data="nsfw_setting")
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data="start")
    )

    return markup


def nsfw_setting_buttons():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="☑️ All Users", callback_data="allowed_for_all_users")
    )
    markup.add(
        InlineKeyboardButton(text="☑️ Only Administrators", callback_data="allowed_only_for_admins")
    )
    markup.add(
        InlineKeyboardButton(text="✅ Only Creator", callback_data="allowed_only_for_creator")
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data="settings")
    )

    return markup