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
ig.load_session_from_file('jackis153', '413431533')



async def youtube_start(message: types.Message):
    await bot.send_message(message.from_user.id, "В каком формате нужно скачать?", reply_markup=client_kb.kb_youtube)
    await FSMAdmin.yt_format.set()
    settings.state_of = 'YouTube'


async def yt_format(message: types.Message, state: FSMContext):
    if message.text in ['Аудио', 'Видео']:
        async with state.proxy() as data:
            data['yt_format'] = message.text
        await FSMAdmin.yt_url.set()
        await bot.send_message(message.from_user.id, "Введите ссылку на видео или плэй-лист", reply_markup=client_kb.kb_cancer)
        settings.state_of = 'YouTube'
    else:
        await bot.send_message(message.from_user.id, "Выберите правильный формат", reply_markup=client_kb.kb_youtube)


async def yt_url(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['yt_link'] = message.text
        result = []
    async with state.proxy() as data:
        for i in tuple(data.values()):
            result.append(i)
    yt = downloaders.youtube.Youtube(result[1], result[0], message)
    if yt.is_true == 0:
        await message.reply("Видео либо плей-лист не найден")
    await yt.send_video_youtube()





@logger.catch()
async def load_ig_link(message: types.Message, state: FSMContext):
    match = re.search(r'/[\w-]{11}', message.text)
    settings.state_of = 'Instagram'
    shortcode = match[0][1:len(match[0]) + 1]
    post = Post.from_shortcode(ig.context, shortcode)
    q = ig.download_post(post, str(message.from_user.id) + '_instagram')
    path = str(message.from_user.id) + '_instagram/'
    if q == True:
        media = []
        ies = []
        caption = ''
        for i in os.listdir(path):
            root, ext = os.path.splitext(path + i)
            if ext in ['.txt']:
                with open(path + i, 'r') as f:
                    caption = f.read()
                    print(caption)
                    # переделать логику
            elif ext in ['.png', '.jpg']:
                print(path + i)
                file = open(path + i, 'rb')
                ies.append(file)
                media.append(InputMediaPhoto(file, caption=caption))
            elif ext in ['.mp4']:
                file = open(path + i, 'rb')
                ies.append(file)
                media.append(InputMediaVideo(file, caption=caption))
        print(media)
        if len(media) >= 2:
            for i in media:
                i.caption = caption
        elif len(media) == 1:
            media[0].caption = ''
            # один caption на всех
        await  bot.send_media_group(message.from_user.id, media)
        for qq in ies:
            qq.close()
        await bot.send_message(message.from_user.id, caption, reply_markup=client_kb.kb_cancer)
        for i in os.listdir(path):
            os.remove(path + i)
        os.rmdir(path)
    else:
        print('False')
        await bot.send_message(settings.admins[0], "Произошла ошибка!!!")
        await bot.send_message(message.from_user.id, "произошла ошибка", reply_markup=client_kb.kb_main_menu)
        for i in os.listdir(path):
            os.remove(path + i)
        os.rmdir(path)
        await state.finish()


async def instagram_start(message: types.Message):
    ig = instaloader.Instaloader()
    ig.load_session_from_file('jackis153', settings.instagram_auth_file_name)
    settings.state_of = 'Instagram'
    await bot.send_message(message.from_user.id, "Введите ссылку на пост, который вы хотите скачать",reply_markup=client_kb.kb_client)
    await FSMAdmin.in_link.set()


async def tik_tok(message: types.Message):
    await bot.send_message(message.from_user.id, "Пока у этой кнопки нет мозгов...",reply_markup=client_kb.kb_client)


async def twitter(message: types.Message):
    await bot.send_message(message.from_user.id, "Пока у этой кнопки нет мозгов...",reply_markup=client_kb.kb_client)


async def cancel_handler(message: types.Message, state: FSMContext):
    await message.reply("Отменено", reply_markup=client_kb.kb_client)
    settings.state_of = None
    await state.finish()


async def main_menu_handler(message: types.Message, state: FSMContext):
    await message.reply('Переход на главное меню.', reply_markup=client_kb.kb_client)
    settings.state_of = None
    await state.finish()


async def spotify(message: types.Message):
    await bot.send_message(message.from_user.id, "Пока у этой кнопки нет мозгов...\nНо я постараюсь вправить их туда:)",reply_markup=client_kb.kb_client)


def register_handlers_keyboard(dp: Dispatcher):
    dp.register_message_handler(cancel_handler, Text(equals=['Отмена'], ignore_case=True), state='*')
    dp.register_message_handler(main_menu_handler, Text(equals=['Вернуться на главное меню'], ignore_case=True),
                                state='*')
    dp.register_message_handler(yt_format, state=FSMAdmin.yt_format)
    dp.register_message_handler(load_ig_link, state=FSMAdmin.in_link)
    dp.register_message_handler(yt_url, state=FSMAdmin.yt_url)

    dp.register_message_handler(youtube_start, Text(equals=['Youtube'], ignore_case=True), state=None)
    dp.register_message_handler(instagram_start, Text(equals=['Instagram'], ignore_case=True), state=None)
    dp.register_message_handler(tik_tok, Text(equals=['TikTok'], ignore_case=True), state=None)
    dp.register_message_handler(twitter, Text(equals=['Twitter'], ignore_case=True), state=None)
    dp.register_message_handler(spotify, Text(equals=['Spotify'], ignore_case=True), state=None)
