import logging
import os

from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

from create_bot import dp
from data_base import sqlite_db
from create_bot import bot
from create_bot import admins
from flask import Flask,request

server=Flask(__name__)

BOT_TOKEN="2135951335:AAF6IpdY-bCHa12E2qzT45mZqCZX250GHRs"
APP_URL='https://total-loader.herokuapp.com/'+BOT_TOKEN
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = 5000
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

server=Flask(__name__)



async def on_startup(dp):
    print("Бот запустился!!!")
    await bot.set_webhook(APP_URL)
    sqlite_db.sql_start()
    for ids in admins:
        await bot.send_message(ids,"Бот запустился")

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    # insert code here to run it before shutdown

    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')



from handlers import client, admin, other, keyboard

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
keyboard.register_handlers_keyboard(dp)
other.register_handlers_other(dp)

if __name__ == '__main__':
    await bot.delete_webhook()
    server.run(host='0.0.0.0',port=os.environ.get("PORT",5000))
    start_webhook(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )


#executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
