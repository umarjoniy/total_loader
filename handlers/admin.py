import os
from speedtest import Speedtest
from aiogram import types, Dispatcher

from settings import admins , logger , download_speed , upload_speed


# class FSMAdmin(StatesGroup):
#     photo = State()
#     name = State()
#     description = State()
#     # price=State()

async def get_log(message:types.Message):
    print(message.text)
    if message.from_user.id in admins:
        logger.debug(f"Getting command {message.text} from user {message.from_user.id})")
        for i in os.listdir():
            logger.debug(f"File: {i}")
        with open('debug.log','rb') as f:
            await message.reply_document(f)

async def get_speed(message:types.Message):
    if message.from_user.id in admins:
        logger.debug(f"Getting command {message.text} from user {message.from_user.id})")
        network=Speedtest(secure=True)
        download_speed=int(network.download()/1024/1024/8)
        upload_speed=int(network.upload()/1024/1024/8)
        await message.reply(f'Download: {download_speed}\nUpload: {upload_speed}')


# # начало диалога загрузки нового пункта меню
# # @dp.message_handler(commands="Загрузить", state=None)
# async def cm_start(message: types.Message):
#     if message.from_user.id in admins:
#         await FSMAdmin.photo.set()
#         await message.reply("Загрузи фото")


# # ловим первый ответ и пишем в словарь
# # @dp.message_handler(content_types=['photo'],state=FSMAdmin.photo)
# async def load_photo(message: types.Message, state: FSMContext):
#     if message.from_user.id in admins:
#         async with state.proxy() as data:
#             data['photo'] = message.photo[0].file_id
#         await FSMAdmin.next()
#         await message.reply("Загрузи имя")


# # ловим второй ответ
# # @dp.message_handler(state=FSMAdmin.name)
# async def load_name(message: types.Message, state: FSMContext):
#     if message.from_user.id in admins:
#         async with state.proxy() as data:
#             data['name'] = message.text
#         await FSMAdmin.next()
#         await message.reply("Введи описание")


# # @dp.message_handler(state=FSMAdmin.description)
# async def load_description(message: types.Message, state: FSMContext):
#     if message.from_user.id in admins:
#         async with state.proxy() as data:
#             data['description'] = message.text
#
#         async with state.proxy() as data:
#             await message.reply(str(data))
#         await state.finish()


# # Выход из состояния
# # dp.message_handler(state="*",commands='отмена')
# # @dp.message_handler(Text(equals='отмена',ignore_case=True),state="*")
# async def cancel_handler(message: types.Message, state: FSMContext):
#     if message.from_user.id in admins:
#         current_state = await state.get_state()
#         if current_state is None:
#             return
#         await state.finish()
#         await message.reply("Ок")


# Регестрируем хэндлеры
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(get_log,commands=["get_log"],state=None)
    dp.register_message_handler(get_speed,commands=["get_speed"],state=None)
    # dp.register_message_handler(cancel_handler, state="*", commands=['отмена'])
    # dp.register_message_handler(cancel_handler, Text(equals=['отмена'], ignore_case=True), state="*")
    # dp.register_message_handler(cm_start, commands=["Загрузить"], state=None)
    # dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    # dp.register_message_handler(load_name, state=FSMAdmin.name)
    # dp.register_message_handler(load_description, state=FSMAdmin.description)
