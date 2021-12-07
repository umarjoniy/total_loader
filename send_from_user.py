import mimetypes
from settings import work_mode
from telethon import TelegramClient

entity = 'video_helper'  # имя сессии - все равно какое
api_id = 13039879
api_hash = '21b5769695be114bde15f8f77e1d9344'
phone = '+79680931979'
client = TelegramClient(entity, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(
        phone)  # при первом запуске - раскомментить, после авторизации для избежания FloodWait советую закомментить
    client.sign_in(phone, input('Enter code: '))
client.start()


async def send_vf(path, message, size, quality, video_name, fps):
    mimetypes.add_type('video/mp4', '.mp4')
    if work_mode == "SERVER":
        await client.send_file('@Total_load_bot', path,
                               caption=str('#'.join([str(message.from_user.id), size, quality, video_name, fps])))
    elif work_mode=="DEBUG":
        await client.send_file('@Tot_load_test_bot', path, caption=str('#'.join([str(message.from_user.id),size,quality,video_name,fps])))
