from aiogram.utils import executor
from create_bot import dp
from data_base import work_with_db
from create_bot import bot
from create_bot import admins


async def on_startup(_):
    print("Бот запустился!!!")
    for ids in admins:
        await bot.send_message(ids, "Бот запустился")


from handlers import client, admin, other, keyboard

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
keyboard.register_handlers_keyboard(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
