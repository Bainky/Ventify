from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram import Bot, Dispatcher

from logging import basicConfig, DEBUG
from data.config import BOT_TOKEN

storage = MemoryStorage()
parse_mode = ParseMode.HTML

bot = Bot(token=BOT_TOKEN, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)

basicConfig(level=DEBUG)