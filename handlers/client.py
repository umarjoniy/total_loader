from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import work_with_db
from aiogram.types import ReplyKeyboardRemove, ContentType


# @dp.message_handler(commands=['start','help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вас приветствует бот для скачивания всего!',
                               reply_markup=kb_client)
        a = work_with_db.check_id(message.from_user.id)
        if a == 'Yes':
            pass
        elif a == 'No':
            work_with_db.add_user(message.from_user.id, message.from_user.username)

    except Exception as e:
        print(e)
        await  message.reply("Общение с ботом ток в ЛС!")


# @dp.message_handler(commands=['Youtube'])
async def open_cafe(message: types.Message):
    await bot.send_message(message.from_user.id, "Работает по субботам!")


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "В Ташкенте!")


async def get_file(message: types.Message):
    x=message.caption.split('#')
    print(x)
    await bot.send_video(int(x[0]),message.video.file_id,caption=x[3])
    work_with_db.youtube_videos(x[3],x[2],x[1],x[4],message.video.file_id)




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(get_file, content_types=ContentType.VIDEO)
    # dp.register_message_handler(open_cafe,commands=['Режим_работы'])
    # dp.register_message_handler(pizza_place_command,commands=['Расположение'])
