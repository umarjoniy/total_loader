import os
import re
from settings import logger
import settings
from settings import FSMAdmin
import instaloader
import downloaders
import pytube
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from aiogram.types import InputMediaVideo, InputMediaPhoto
from instaloader import Post

from create_bot import bot
from keyboards import client_kb

# from aiogram.types import ReplyKeyboardRemove
ig = instaloader.Instaloader()
ig.load_session_from_file('jackis153','413431533')

# Я думаю, нам не нужна эта функция!
async def yt_format(message: types.Message, state: FSMContext):
    if message.text in ['Аудио','Видео']:
        async with state.proxy() as data:
            data['yt_format']=message.text
        await FSMAdmin.yt_link.set()
        await bot.send_message(message.from_user.id,"Введите ссылку",reply_markup=client_kb.kb_cancer)
    else:
        await bot.send_message(message.from_user.id,"Выберите правильный формат",reply_markup=client_kb.kb_youtube)

# переписать логику
async def youtube_start(message: types.Message):
    # Долго чекает!
    await bot.send_message(message.from_user.id,"В каком формате нужно скачать?",reply_markup=client_kb.kb_youtube)
    await FSMAdmin.yt_format.set()
    # await bot.send_message(message.from_user.id,
    #                        "Введите ссылку на одно видео(ничего кроме видео)",reply_markup=client_kb.kb_cancer)  # reply_markup=ReplyKeyboardRemove()
    # await FSMAdmin.yt_link.set()
#добавить состояния типа отправляет печатает читает
@logger.catch()
async def load_ig_link(message: types.Message, state: FSMContext):
    match = re.search(r'/[\w-]{11}', message.text)
    shortcode = match[0][1:len(match[0]) + 1]
    post = Post.from_shortcode(ig.context, shortcode)
    q = ig.download_post(post,str(message.from_user.id)+'_instagram')
    if q==True:
        media = []
        ies=[]
        caption=''
        path = str(message.from_user.id) + '_instagram/'
        for i in os.listdir(path):
            root,ext=os.path.splitext(path+i)
            if ext in ['.txt']:
                with open(path+i,'r') as f:
                    caption=f.read()
                    print(caption)
                    #переделать логику
            elif ext in ['.png','.jpg']:
                print(path+i)
                file=open(path+i,'rb')
                ies.append(file)
                media.append(InputMediaPhoto(file,caption=caption))
            elif (path + i)[len(path+i)-3:] in ['.mp4']:
                file=open(path + i, 'rb')
                ies.append(file)
                media.append(InputMediaVideo(file,caption=caption))
        print(media)
        for i in media:
            i.caption=caption
            #один caption на всех
        await  bot.send_media_group(message.from_user.id,media)
        for qq in ies:
            qq.close()
        await bot.send_message(message.from_user.id,caption,reply_markup=client_kb.kb_cancer)
        for i in os.listdir(path):
            os.remove(path+i)
        os.rmdir(path)
    else:
        print('False')
        await bot.send_message(settings.admins[0],"Произошла ошибка!!!")
        await bot.send_message(message.from_user.id,"произошла ошибка",reply_markup=client_kb.kb_client)
        await state.finish()


async def yt_url(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['yt_link'] = message.text
        await FSMAdmin.yt_link.set()
        result=[]
    async with state.proxy() as data:
        for i in tuple(data.values()):
            result.append(i)
    yt=downloaders.youtube.Youtube(result[1],result[0],message)
    if yt.is_true==0:
        await message.reply("Видео либо плей-лист не найден")
    else:
        await state.finish()
    await yt.send_video()


async def instagram_start(message: types.Message):
    #await bot.send_message(message.from_user.id,'Пока это не работает')
    ig = instaloader.Instaloader()
    ig.load_session_from_file('jackis153',settings.instagram_auth_file_name)
    await bot.send_message(message.from_user.id,"Введите ссылку на пост, который вы хотите скачать")
    await FSMAdmin.in_link.set()
    #post = Post.from_shortcode(ig.context, a)
    #q = ig.download_post(post, 'name')


async def tik_tok(message: types.Message):
    await bot.send_message(message.from_user.id, "Пока у этой кнопки нет мозгов...")


async def twitter(message: types.Message):
    await bot.send_message(message.from_user.id, "Пока у этой кнопки нет мозгов...")


async def cancel_handler(message: types.Message, state: FSMContext):
    await message.reply("Отменено", reply_markup=client_kb.kb_client)
    await state.finish()

async def main_menu_handler(message:types.Message,state:FSMContext):
    await message.reply('Переход на главное меню.',reply_markup=client_kb.kb_client)
    await state.finish()

async def spotify(message:types.Message):
    await bot.send_message(message.from_user.id, "Пока у этой кнопки нет мозгов...\nНо я постараюсь вправить их туда:)")

def register_handlers_keyboard(dp: Dispatcher):
    dp.register_message_handler(youtube_start, Text(equals=['Youtube'], ignore_case=True), state=None)
    dp.register_message_handler(instagram_start, Text(equals=['Instagram'], ignore_case=True), state=None)
    dp.register_message_handler(tik_tok, Text(equals=['TikTok'], ignore_case=True), state=None)
    dp.register_message_handler(twitter, Text(equals=['Twitter'], ignore_case=True), state=None)
    dp.register_message_handler(spotify, Text(equals=['Spotify'], ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler,Text(equals=['Отмена'], ignore_case=True), state='*')
    dp.register_message_handler(main_menu_handler,Text(equals=['Вернуться на главное меню'], ignore_case=True), state='*')
    dp.register_message_handler(yt_format, state=FSMAdmin.yt_format)
    dp.register_message_handler(load_ig_link, state=FSMAdmin.in_link)
    dp.register_message_handler(yt_url, state=FSMAdmin.yt_link)
