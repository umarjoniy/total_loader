import os

import aiogram
import pytube
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from pytube import YouTube
from settings import logger, download_speed, upload_speed
from keyboards import client_kb
import send_from_user
from create_bot import bot
# from aiogram.types import ReplyKeyboardRemove
from data_base import work_with_db

#надо до конца продолжить машину состояний(до скачивания видео и отправки)
class FSMAdmin(StatesGroup):
    link = State()

@logger.catch
async def youtube(message: types.Message, url):
    try:
        yt = YouTube(url)
    except pytube.exceptions.RegexMatchError:
        return 'Not exist'
    # Когда мы получаем не ссылку в Ютуб- вылетает ошибка
    #Реализовать команду get_log для админов
    #добавить логи на то, что кто отправлял
    size = str(yt.streams.get_highest_resolution().filesize)
    quality = yt.streams.get_highest_resolution().resolution
    video_name = yt.streams.get_highest_resolution().title
    fps = str(yt.streams.get_highest_resolution().fps)
    logger.debug(f"Size: {size}B({str(int(size)/1024/1024)}MB), quality: {quality}, videos name: {video_name}, fps: {str(fps)}")

    if (int(size) / 1024 / 1024) < 370:
        file_id = work_with_db.check_youtube_video(video_name, quality, fps)
        logger.debug(f"File id: {file_id}")
        if str(file_id) == '0':
            logger.debug("Downloading youtube video")
            a = await bot.send_message(message.from_user.id,"Видео скачивается на сервер...")
            path = yt.streams.get_highest_resolution().download()
            await bot.edit_message_text(f"Видео отпправляется.\nОжидайте примерно {int(int(int(int(size)/1024/1024)/upload_speed)/60+1)} минут(у)",message.from_user.id,a.message_id)
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
                work_with_db.youtube_videos_delete(video_name,quality,fps)
                await youtube(message,url)
    else:
        await bot.send_message(message.from_user.id, 'Размер видео больше чем 370МБ(техническое ограничение)')
        return "not Found"


# Я думаю, нам не нужна эта функция!
async def load_link(message: types.Message, state: FSMContext):
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
    await FSMAdmin.link.set()


async def instagram(message: types.Message):
    await bot.send_message(message.from_user.id, "Пока у этой кнопки нет мозгов...")


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

def register_handlers_keyboard(dp: Dispatcher):
    dp.register_message_handler(youtube_start, Text(equals=['Youtube'], ignore_case=True), state=None)
    dp.register_message_handler(instagram, Text(equals=['Instagram'], ignore_case=True), state=None)
    dp.register_message_handler(tik_tok, Text(equals=['TikTok'], ignore_case=True), state=None)
    dp.register_message_handler(twitter, Text(equals=['Twitter'], ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler,Text(equals=['Отмена'], ignore_case=True), state='*')
    dp.register_message_handler(main_menu_handler,Text(equals=['Вернуться на главное меню'], ignore_case=True), state='*')
    dp.register_message_handler(load_link, state=FSMAdmin.link)
