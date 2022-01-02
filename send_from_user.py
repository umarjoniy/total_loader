import mimetypes
from settings import server_accaunts, debug_accaunts
from settings import work_mode
from telethon import TelegramClient
import os

if work_mode == "SERVER":
    client = TelegramClient(server_accaunts.get('entity'), server_accaunts.get('api_id'),
                            server_accaunts.get('api_hash'))
elif work_mode == 'DEBUG':
    client = TelegramClient(debug_accaunts.get('entity'), debug_accaunts.get('api_id'),
                            debug_accaunts.get('api_hash'))
client.connect()
if not client.is_user_authorized():
    if work_mode == "SERVER":
        client.send_code_request(server_accaunts.get('phone'))
        client.sign_in(server_accaunts.get('phone'), input('Enter code: '))
    elif work_mode == 'DEBUG':
        client.send_code_request(debug_accaunts.get('phone'))
        client.sign_in(debug_accaunts.get('phone'), input('Enter code: '))
client.start()


async def send_vf(path, message, size, quality, video_name, fps,type):
    mimetypes.add_type('video/mp4', '.mp4')
    if work_mode == "SERVER":

        await client.send_file('@Total_load_bot', path,
                               caption=str('#'.join([str(message.from_user.id), size, quality, video_name, fps,type])))
    elif work_mode == "DEBUG":
        await client.send_file('@Tot_load_test_bot', path,voice_note=True,
                               caption=str('#'.join([str(message.from_user.id), size, quality, video_name, fps,type])))
