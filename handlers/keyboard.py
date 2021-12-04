import os

from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from pytube import YouTube
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot, admins
import send_from_user
from aiogram.types.input_file import InputFile


class FSMAdmin(StatesGroup):
    link = State()


# def on_complete(info,path):
#     os.remove(path)


async def youtubee(message: types.Message, url):
    await FSMAdmin.link.set()

    yt = YouTube(url)
    name = yt.streams.get_highest_resolution().download()
    await send_from_user.send_vf(name, message)
    os.remove(name)


async def load_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
        await youtubee(message, message.text)
    # async with state.proxy() as data:
    # await message.reply(str(data))
    await state.finish()


async def insta(message: types.Message):
    await  bot.send_video(message.from_user.id,
                          'BAACAgIAAxkBAAIDWmGrP4tqHYpkiU8TOVXKlStliAqtAALtEQACkwZYSYfZIS7Dz-h0IgQ')


async def from_keyboard(message: types.Message):
    if message.text == ("Youtube"):
        await bot.send_message(message.from_user.id, "Скачать с Youtube")  # reply_markup=ReplyKeyboardRemove()
        await FSMAdmin.link.set()
        # bot.send_video(message.from_user.id,'https://r360102.kujo-jotaro.com/naruto/3/78.480.687f820dd24995f0.mp4?hash1=06bec7baeadd70d2e48bf6838842832d')
    elif message.text == ("Instagram"):
        pass


def register_handlers_keyboard(dp: Dispatcher):
    dp.register_message_handler(insta, Text(equals=['Instagram'], ignore_case=True), state="*")
    dp.register_message_handler(from_keyboard, Text(equals=['Youtube'], ignore_case=True), state=None)
    dp.register_message_handler(load_link, state=FSMAdmin.link)
