from aiogram import types, Dispatcher
from aiogram.types import ContentType

from create_bot import bot
from data_base import work_with_db
from keyboards import client_kb
from settings import video_get_accaunt, logger


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вас приветствует бот для скачивания всего!\nБот находится на альфа-тесте',
                               reply_markup=client_kb.kb_client)
        a = work_with_db.check_id(message.from_user.id)
        if a == 'Yes':
            pass
        elif a == 'No':
            work_with_db.add_user(message.from_user.id, message.from_user.username)

    except Exception as e:
        print(e)
        await  message.reply("Общение с ботом ток в ЛС!")


@logger.catch()
async def get_file(message: types.Message):
    logger.info(message.from_user.id)
    logger.info(video_get_accaunt)
    if message.from_user.id in video_get_accaunt:
        x = message.caption.split('#')
        logger.debug(f"Got datas:{x}")
        if x[5]=="Аудио":
            await bot.send_voice(int(x[0]),message.voice.file_id,caption=x[3],reply_markup=client_kb.kb_main_menu)
            work_with_db.youtube_videos(x[3], x[2], x[1], x[4], message.voice.file_id)
        else:
            await bot.send_video(int(x[0]), message.video.file_id, caption=x[3],reply_markup=client_kb.kb_main_menu)
            work_with_db.youtube_videos(x[3], x[2], x[1], x[4], message.video.file_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(get_file, content_types=ContentType.VIDEO)
    dp.register_message_handler(get_file, content_types=ContentType.VOICE)
