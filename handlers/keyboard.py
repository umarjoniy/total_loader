import os

import aiogram
import re
import instaloader
from aiogram.types import InputMediaVideo, InputMediaPhoto
from instaloader import Post
import pytube
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from pytube import YouTube
import settings
from keyboards import client_kb
import send_from_user
from create_bot import bot
# from aiogram.types import ReplyKeyboardRemove
from data_base.work_with_db import *
ig = instaloader.Instaloader()
ig.load_session_from_file('jackis153','413431533')

class FSMAdmin(StatesGroup):
    yt_link = State()
    in_link=State()

@logger.catch
async def youtube(message: types.Message, url):
    try:
        yt = YouTube(url)
        logger.debug(url)
    except pytube.exceptions.RegexMatchError:
        return 'Not exist'
    size = str(yt.streams.get_highest_resolution().filesize)
    quality = yt.streams.get_highest_resolution().resolution
    video_name = yt.streams.get_highest_resolution().title
    fps = str(yt.streams.get_highest_resolution().fps)
    logger.debug(f"Size: {size}B({str(int(size)/1024/1024)}MB), quality: {quality}, videos name: {video_name}, fps: {str(fps)}")

    if (int(size) / 1024 / 1024) < 370:
        file_id = check_youtube_video(video_name, quality, fps)
        logger.debug(file_id)
        logger.debug(f"File id: {file_id}")
        if str(file_id) == '0':
            logger.debug("Downloading youtube video")
            a = await bot.send_message(message.from_user.id,"Видео скачивается на сервер...")
            path = yt.streams.get_highest_resolution().download()
            await bot.edit_message_text(f"Видео отпправляется.\nОжидайте",message.from_user.id,a.message_id)
            logger.debug("Downloaded!")
            await send_from_user.send_vf(path, message, size, quality, video_name, fps)
            await bot.delete_message(message.from_user.id,a.message_id)
            os.remove(path)
        elif str(file_id) == "Error":
            await bot.send_message(message.from_user.id, 'Произошла ошибка!')
        else:
            try:
                await bot.send_video(message.from_user.id, file_id[0], caption=video_name)

            except aiogram.utils.exceptions.WrongFileIdentifier:
                logger.info(f"File id {file_id[0]} is old?")
                youtube_videos_delete(video_name,quality,fps)
                await youtube(message,url)
    else:
        await bot.send_message(message.from_user.id, 'Размер видео больше чем 370МБ(техническое ограничение)')
        return "not Found"


# Я думаю, нам не нужна эта функция!
async def load_yt_link(message: types.Message, state: FSMContext):
    a = await youtube(message, message.text)
    if a == 'Not exist':
        await  bot.send_message(message.from_user.id, "Отправленное видео не найдено либо не доступно(")
        del a
    elif a=="not Found":
        pass


# переписать логику
async def youtube_start(message: types.Message):
    # Долго чекает!
    await bot.send_message(message.from_user.id,
                           "Введите ссылку на одно видео(ничего кроме видео)",reply_markup=client_kb.kb_cancer)  # reply_markup=ReplyKeyboardRemove()
    await FSMAdmin.yt_link.set()
#добавить состояния типа отправляет печатает читает
async def load_ig_link(message: types.Message, state: FSMContext):
    match = re.search(r'/[\w-]{11}', message.text)
    shortcode = match[0][1:len(match[0]) + 1]
    post = Post.from_shortcode(ig.context, shortcode)
    q = ig.download_post(post,str(message.from_user.id)+'i')
    if q==True:
        media = []
        caption=''
        path = str(message.from_user.id) + 'i/'
        for i in os.listdir(str(message.from_user.id)+'i'):
            if (path + i)[len(path+i)-3:] in ['txt']:
                with open(path+i,'r') as f:
                    caption=f.read()
                    print(caption)
                    #переделать логику
            elif (path + i)[len(path+i)-3:] in ['png','jpg']:
                print(path+i)
                media.append(InputMediaPhoto(path+i,caption=caption))
            elif (path + i)[len(path+i)-3:] in ['mp4']:
                media.append(InputMediaVideo(path+i,caption=caption))
        print(media)
        await  bot.send_media_group(message.from_user.id,media)
        os.remove(path)
        await state.finish()
    else:
        print('False')
        await state.finish()





async def instagram_start(message: types.Message):
    await bot.send_message(message.from_user.id,'Пока это не работает')
    # ig = instaloader.Instaloader()
    # ig.load_session_from_file('jackis153',settings.instagram_auth_file_name)
    # await bot.send_message(message.from_user.id,"Введите ссылку на пост, который вы хотите скачать")
    # await FSMAdmin.in_link.set()
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
    dp.register_message_handler(load_yt_link, state=FSMAdmin.yt_link)
    dp.register_message_handler(load_ig_link, state=FSMAdmin.in_link)
