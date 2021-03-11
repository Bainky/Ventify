from .connector import users, groups
from .. import clean_dict


async def chat_exists(collection, filter):
    """
    If the chat ID is found in the database, then the function returns the True.
    :param message: object_exists(users, {"id": message.chat.id})
    """
    return await collection.find_one(filter)


async def register_chat(message):
    """
    Function for registering users.
    For collecting statistics, for example, 
    in order to find out how many users are using the bot.
    Can also be used to send out something

    :param: register_chat(arguments)
    """
    chat = message.chat
    date = message.date
    user = message.from_user

    filter = {"chat.id": chat.id}

    if chat.type == "private":

        collection = users

        document = {
            "chat": {
                "id": user.id,
                "is_bot": user.is_bot,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "language_code": user.language_code
            },
            "settings": {
                "language": False,
            },
            "date": date
        }
    
    if chat.type in ["group",  "supergroup"]:

        collection = groups

        document = {
            "chat": {
                "id": chat.id,
                "title": chat.title,
                "username": chat.username,
                "type": chat.type
            },
            "settings": {
                "language": False,
                "nsfw": {
                    "all": False,
                    "admins": True,
                    "owner": True,
                },
            },
            "date": date
        }

    # If the user is not in the database
    if not await chat_exists(collection, filter):
        await collection.insert_one(clean_dict(document))