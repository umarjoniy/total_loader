from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base.sqlite_db import check_id,sql_add_command
from aiogram.types import ReplyKeyboardRemove, ContentType


# @dp.message_handler(commands=['start','help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вас приветствует бот для скачивания всего!',
                               reply_markup=kb_client)
        a=check_id(message.from_user.id)
        if a=='Yes':
            pass
        elif a=='No':
            sql_add_command(message.from_user.id, message.from_user.username)

    except Exception as e:
        print(e)

        await  message.reply("Общение с ботом ток в ЛС!")

# @dp.message_handler(commands=['Youtube'])
async def open_cafe(message: types.Message):
    await bot.send_message(message.from_user.id, "Работает по субботам!")


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "В Ташкенте!")


async def get_file(message:types.Message):
    print(message)
    temp=await bot.forward_message(int(message.caption),message.from_user.id,message.message_id)
    print(temp)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(get_file,content_types=ContentType.VIDEO)
    # dp.register_message_handler(open_cafe,commands=['Режим_работы'])
    # dp.register_message_handler(pizza_place_command,commands=['Расположение'])
