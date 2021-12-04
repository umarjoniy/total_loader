from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from pytube import YouTube
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot, admins
import from_yt_download
from aiogram.types.input_file import InputFile




class FSMAdmin(StatesGroup):
    link = State()


async def youtubee(message: types.Message, url):
    await FSMAdmin.link.set()

    yt = YouTube(url)
    name= yt.streams.get_lowest_resolution().download()
    print(name)
    await from_yt_download.send_vf(name,message)


async def youtube(message: types.Message):
    await FSMAdmin.link.set()
    # b = yt.streams.get_highest_resolution().get_url()
    # = InputFile.from_url(
    #    b,
    #    filename="python-logoo.mp4"
    # )
    # f=open(image,'rb')
    # print(image)
    # await bot.send_document(message.from_user.id,image)
    # msg=await client.send_file('@py_hack06',image,caption="5")
    # print(msg)
    #client.disconnect()
    # await bot.send_document(message.from_user.id,msg)
    # f.close()


async def load_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
        tot_url = message.text
        await youtubee(message, message.text)
    # async with state.proxy() as data:
    # await message.reply(str(data))
    await state.finish()


async def insta():
    pass


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
