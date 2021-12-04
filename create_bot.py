from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


admins=[413431533]


#1106300203

storage=MemoryStorage()

bot = Bot('2135951335:AAF6IpdY-bCHa12E2qzT45mZqCZX250GHRs')#real bot
#bot=Bot('5058648135:AAH39A6kIFKu3A7PlcqeRnG0wmvWtqy-sGU')#test bot
dp = Dispatcher(bot, storage=storage)
