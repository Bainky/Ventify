from . import create_session


async def valid_object_size(session, image):
    """
    Telegram cannot handle more photos more than 5MB.
    If you remove this check, the preview may not be displayed
    with some references on which the photo exceeds limit.
    """
    async with session.get(image) as r:
        # Get the size of photos on the page
        file_size = r.headers["Content-Length"]
        # Close the current session
        await session.close()
        # If photo is too big
        if int(file_size) > 5242880:
            return True


async def get_object(object, attribute):
    """
    Sending requests to api websites with pictures.
    Returns just a link to the file.
    """
    session = create_session()
    # Send a request to get a link to image
    async with session.get(object) as r:
        query = await r.json()

    # image link is here
    image = query[attribute]

    # If the image fails the size check
    if await valid_object_size(session, image):
        # We send another request for api
        return await get_object(object, attribute)

    return image
