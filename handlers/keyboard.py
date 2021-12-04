import os
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from data_base import work_with_db
from pytube import YouTube
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot, admins
import send_from_user



class FSMAdmin(StatesGroup):
    link = State()


# def on_complete(info,path):
#     os.remove(path)


async def youtubee(message: types.Message, url):
    yt = YouTube(url)
    size = str(yt.streams.get_highest_resolution().filesize)
    quality=yt.streams.get_highest_resolution().resolution
    video_name=yt.streams.get_highest_resolution().title
    fps=str(yt.streams.get_highest_resolution().fps)
    print(size,quality,video_name,fps)
    path=None

    if (int(size)/1024/1024) <370:
        file_id=work_with_db.check_youtube_video(video_name,quality,fps)
        print(file_id)
        if str(file_id)=='0':
            path = yt.streams.get_highest_resolution().download()
            await send_from_user.send_vf(path, message,size,quality,video_name,fps)
            os.remove(path)
        else:
            await bot.send_video(message.from_user.id,file_id[0],caption=video_name)
            os.remove(path)


    else:
        await bot.send_message(message.from_user.id,'Размер видео больше чем 370МБ(техническое ограничение)')


async def load_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
        await youtubee(message, message.text)
    # async with state.proxy() as data:
    # await message.reply(str(data))
    await state.finish()


async def insta(message: types.Message):
    pass


async def from_keyboard(message: types.Message):
    if message.text == ("Youtube"):
        await bot.send_message(message.from_user.id, "Введите ссылку на одно видео(ничего кроме видео)")  # reply_markup=ReplyKeyboardRemove()
        await FSMAdmin.link.set()
    elif message.text == ("Instagram"):
        pass


def register_handlers_keyboard(dp: Dispatcher):
    dp.register_message_handler(insta, Text(equals=['Instagram'], ignore_case=True), state="*")
    dp.register_message_handler(from_keyboard, Text(equals=['Youtube'], ignore_case=True), state=None)
    dp.register_message_handler(load_link, state=FSMAdmin.link)
