from aiogram import Dispatcher


async def on_shutdown_close_db(dp: Dispatcher):
    """
    Close memory storage
    """
    await dp.storage.close()
    await dp.storage.wait_closed()