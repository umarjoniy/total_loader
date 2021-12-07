from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings import work_mode

storage = MemoryStorage()
bot = None
if work_mode == "SERVER":
    from settings import server_bot
    bot = Bot(server_bot)  # real bot
elif work_mode == "DEBUG":
    from settings import test_bot
    bot = Bot(test_bot)

dp = Dispatcher(bot, storage=storage)
