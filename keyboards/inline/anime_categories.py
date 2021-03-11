from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def anime_choose_safe_category():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="🔒 SFW", callback_data="sfw"),
        InlineKeyboardButton(text="🔞 NSFW", callback_data="nsfw")
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data="menu")
    )

    return markup


def anime_sfw_categories():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="💃🏼 Anime", callback_data="anime")
    )
    markup.add(
        InlineKeyboardButton(text="🌺 Waifu", callback_data="waifu"),
        InlineKeyboardButton(text="🦊 Neko", callback_data="neko")
    )
    markup.add(
        InlineKeyboardButton(text="🎭 D.VA", callback_data="dva"),
        InlineKeyboardButton(text="🧛🏻 Shinobu", callback_data="shinobu"),
        InlineKeyboardButton(text="🧙🏻‍♀️ Megumin", callback_data="megumin")
    )
    markup.add(
        InlineKeyboardButton(text="👄 Bite", callback_data="bite"),
        InlineKeyboardButton(text="💋 Kiss", callback_data="kiss"),
        InlineKeyboardButton(text="👅 Lick", callback_data="lick"),
    )
    markup.add(
        InlineKeyboardButton(text="🤗 Cuddle", callback_data="cuddle"),
        InlineKeyboardButton(text="🤗 Glomp", callback_data="glomp"),
        InlineKeyboardButton(text="🤗 Wink", callback_data="wink"),
    )
    markup.add(
        InlineKeyboardButton(text="🧸 Pat", callback_data="pat"),
        InlineKeyboardButton(text="😏 Smug", callback_data="smug"),
        InlineKeyboardButton(text="😈 Bonk", callback_data="bonk")
    )
    markup.add(
        InlineKeyboardButton(text="💨 Yeet", callback_data="yeet"),
        InlineKeyboardButton(text="☺ Blush", callback_data="blush"),
        InlineKeyboardButton(text="😀 Smile", callback_data="smile"),
    )
    markup.add(
        InlineKeyboardButton(text="👋 Wave", callback_data="wave"),
        InlineKeyboardButton(text="🖐 Highfive", callback_data="highfive"),
        InlineKeyboardButton(text="✊ Handhold", callback_data="handhold")
    )
    markup.add(
        InlineKeyboardButton(text="🍕 Nom", callback_data="nom"),
        InlineKeyboardButton(text="🩸 Kill", callback_data="kill"),
        InlineKeyboardButton(text="👋 Slap", callback_data="slap"),
    )
    markup.add(
        InlineKeyboardButton(text="😄 Happy", callback_data="happy"),
        InlineKeyboardButton(text="😭 Cry", callback_data="cry"),
        InlineKeyboardButton(text="😜 Poke", callback_data="poke"),
    )
    markup.add(
        InlineKeyboardButton(text="🕺 Dance", callback_data="dance"),
        InlineKeyboardButton(text="😅 Cringe", callback_data="cringe"),
        InlineKeyboardButton(text="🥖 Baguette", callback_data="baguette")
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data="anime")
    )

    return markup


def anime_nsfw_categories():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton(text="🍓 Hentai", callback_data="hentai"),
    )
    markup.add(
        InlineKeyboardButton(text="🍫 Waifu", callback_data="nsfw_waifu"),
        InlineKeyboardButton(text="🎀 Neko", callback_data="nsfw_neko"),
    )
    markup.add(
        InlineKeyboardButton(text="🍌 Trap", callback_data="trap"),
        InlineKeyboardButton(text="👙 Yuri", callback_data="yuri"),
    )
    markup.add(
        InlineKeyboardButton(text="🤝 Blowjob", callback_data="blowjob"),
    )
    markup.add(
        InlineKeyboardButton(text="🔙 Back", callback_data="anime")
    )

    return markup