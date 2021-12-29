from loguru import logger
from aiogram.dispatcher.filters.state import State, StatesGroup
logger.add('debug.log', format="{time} {level} {message}", level='DEBUG', rotation='15MB', compression='zip')
from speedtest import Speedtest
network=Speedtest(secure=True)
admins=[413431533,1106300203]
instagram_auth_file_name='413431533'
video_get_accaunt=[2106956112]
debug_accaunts={'entity': "Project",'api_hash':'2ce977d528d6020fc69177a5b7de0f53','api_id':3775421,'phone':'+998909423844'}
server_accaunts={'entity': "video_helper",'api_hash':'21b5769695be114bde15f8f77e1d9344','api_id':13039879,'phone':'+79680931979'}
work_mode='SERVER'#'SERVER',DEBUG
server_bot='2135951335:AAF6IpdY-bCHa12E2qzT45mZqCZX250GHRs'
test_bot='5058648135:AAH39A6kIFKu3A7PlcqeRnG0wmvWtqy-sGU'
#upload_speed=int(network.upload()/1024/1024)
#download_speed=int(network.download()/1024/1024)

class FSMAdmin(StatesGroup):
    yt_link = State()
    yt_format=State()
    in_link=State()