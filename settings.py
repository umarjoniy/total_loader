from loguru import logger
logger.add('debug.log', format="{time} {level} {message}", level='DEBUG', rotation='15MB', compression='zip')
from speedtest import Speedtest
network=Speedtest(secure=True)
admins=[413431533]
instagram_auth_file_name='413431533'
video_get_accaunt=[2106956112]
work_mode='SERVER'#'SERVER',DEBUG
server_bot='2135951335:AAF6IpdY-bCHa12E2qzT45mZqCZX250GHRs'
test_bot='5058648135:AAH39A6kIFKu3A7PlcqeRnG0wmvWtqy-sGU'
#upload_speed=int(network.upload()/1024/1024)
#download_speed=int(network.download()/1024/1024)