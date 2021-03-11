from aiogram.utils.markdown import hide_link
from aiogram.types import CallbackQuery

from loader import dp
from utils import (
    get_object,
    get_attributes_of_object
)
from keyboards import (
    anime_choose_safe_category,
    anime_sfw_categories,
    anime_nsfw_categories,
    animals_categories,
    menu_with_categories,
    control_buttons
)


@dp.callback_query_handler(text="menu")
async def call_menu_with_categories(call: CallbackQuery):
    """
    Function for sending a menu,
    with a selection of safe content
    """
    await call.answer()
    # Editing the message
    await call.message.edit_text(
        text=(
            "<b>🔗 Select a category to get a picture.</b>"
        ),
        reply_markup=menu_with_categories()
    )


@dp.callback_query_handler(text="anime")
async def call_anime_categories(call: CallbackQuery):
    """
    Redirect to select anime actions
    """
    await call.answer()
    # Editing the message
    await call.message.edit_text(
        text=(
            "<b>⚜️ Choose what content you want to see.</b>"
        ),
        reply_markup=anime_choose_safe_category()
    )


@dp.callback_query_handler(text=["sfw", "nsfw"])
async def call_nsfw_categories(call: CallbackQuery):
    """
    Redirect to anime content
    """
    data = call.data.upper()
    message = call.message

    # Send answer
    await call.answer()

    if data == "SFW":
        kb = anime_sfw_categories()
    else:
        kb = anime_nsfw_categories()

    # Editing the message
    await message.edit_text(
        text=(
            f"<b>🍿 You are in the {data} category.</b>"
        ),
        reply_markup=kb
    )


@dp.callback_query_handler(text="animals")
async def call_anime_categories(call: CallbackQuery):
    """
    Redirect to animals content
    """
    await call.answer()
    # Editing the message
    await call.message.edit_text(
        text=(
            "<b>🦄 You are in the category with animals.</b>"
        ),
        reply_markup=animals_categories()
    )


@dp.callback_query_handler()
async def call_get_photography(call: CallbackQuery):
    """
    Function for sending photos
    """
    message = call.message
    data = call.data

    # Get json document
    api = get_attributes_of_object()

    if data == "generate_new":
        data = message.text.split("#")[1]

    obj = api[data]["object"]
    atr = api[data]["attribute"]
    mark = api[data]["entity"]

    if mark == "anime":
        mark = api[data]["safe"]

    if mark == "memes":
        mark = "menu"

    # We get a link to the preview photo
    link = await get_object(obj, atr)

    await call.answer()
    # Editing the message
    await message.edit_text(
        text=(
            f"{hide_link(link)} #{data}"
        ),
        reply_markup=control_buttons(mark)
    )