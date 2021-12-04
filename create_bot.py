from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


admins=[413431533]


#1106300203

storage=MemoryStorage()

bot = Bot('2135951335:AAF6IpdY-bCHa12E2qzT45mZqCZX250GHRs')
dp = Dispatcher(bot, storage=storage)
