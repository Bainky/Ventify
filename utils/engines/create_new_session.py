from aiohttp import ClientSession


def create_session():
    """
    Creation of a new session.
    Required to send requests to the api.
    """
    return ClientSession(
        headers={
            "User-Agent": "bot"
        }
    )