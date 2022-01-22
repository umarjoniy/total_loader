import mimetypes

import create_bot
import settings

client = None
import telethon
from aiogram import types
from settings import server_accaunts, debug_accaunts
from settings import work_mode
from telethon import TelegramClient, events, sync
import os


def activate_acc(message: types.Message = None):
    global client
    if work_mode == "SERVER":
        client = TelegramClient(server_accaunts.get('entity'), server_accaunts.get('api_id'),
                                server_accaunts.get('api_hash'))
    elif work_mode == 'DEBUG':
        client = TelegramClient(debug_accaunts.get('entity'), debug_accaunts.get('api_id'),
                                debug_accaunts.get('api_hash'))
    client.connect()

    if not client.is_user_authorized():
        if work_mode == "SERVER":
            hash=client.send_code_request(server_accaunts.get('phone'))
            code = input("Введите код:\n")
            client.sign_in(server_accaunts.get('phone'), code, password='Umarjoniy2006',phone_code_hash=hash)
        elif work_mode == 'DEBUG':
            hash=client.send_code_request(server_accaunts.get('phone'))
            code=input("Введите код:\n")
            client.sign_in(debug_accaunts.get('phone'), code, password='Umarj0niy2oo6',phone_code_hash=hash)

    try:
        client.start()
    except telethon.errors.rpcerrorlist.AuthKeyDuplicatedError:
        os.remove('video_helper.session')
        try:
            os.remove('Project.session')
        except:
            pass
        activate_acc()


activate_acc()


async def send_vf(path, message, size, quality, video_name, fps, type):
    mimetypes.add_type('video/mp4', '.mp4')
    global client
    if work_mode == "SERVER":
        await client.send_file('@Total_load_bot', path,
                               caption=str('#'.join([str(message.from_user.id), size, quality, video_name, fps, type])))
    elif work_mode == "DEBUG":
        await client.send_file('@Tot_load_test_bot', path, voice_note=True,
                               caption=str('#'.join([str(message.from_user.id), size, quality, video_name, fps, type])))
