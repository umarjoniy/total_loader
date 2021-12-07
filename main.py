from aiogram.utils import executor
from settings import logger
from create_bot import bot
from create_bot import dp
from settings import admins
from keyboards import kb_client


async def on_startup(_):
    logger.info('bot are working')
    for ids in admins:
        await bot.send_message(ids, "Бот запустился",reply_markup=kb_client)


from handlers import client, other, keyboard

client.register_handlers_client(dp)
#admin.register_handlers_admin(dp)
keyboard.register_handlers_keyboard(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
