import sys

from telethon.sync import TelegramClient
from telethon.tl.types import DocumentAttributeAudio
import mimetypes
entity = 'video_helper' #имя сессии - все равно какое
api_id = 13039879
api_hash = '21b5769695be114bde15f8f77e1d9344'
phone =  '+79680931979'
client = TelegramClient(entity, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone) #при первом запуске - раскомментить, после авторизации для избежания FloodWait советую закомментить
    client.sign_in(phone, input('Enter code: '))
client.start()
# a=client.upload_file('https://r3---sn-n8v7zns7.googlevideo.com/videoplayback?expire=1638568351&ei=Pz2qYcj0HNOPv_IPzI68qAk&ip=91.231.57.124&id=o-AMh3NEtdtyIzVW4reoIfnqi_jXspTwtRfKWIBQKuKyLe&itag=22&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ns=wmRxhcv80t9G_V-aWJgxBFcG&cnr=14&ratebypass=yes&dur=936.066&lmt=1638530764035325&fexp=24001373,24007246&c=WEB&txp=4432434&n=4VwLzUcNDjcANXCDpz&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgSe8hr3H-4EFLA1zB3qT47RrSBVV88HezgApQkiSVkU0CIAr0q2F4bjXDAOlNxHEKY9Ivr1M7YHvevwQcciSrpKop&cm2rm=sn-b5an01-u5ne7s&req_id=89241a81a28ba3ee&redirect_counter=2&rm=sn-ug5onuxaxjvh-n8v67s&cms_redirect=yes&hcs=sd&mh=m4&mm=30&mn=sn-n8v7zns7&ms=nxu&mt=1638546277&mv=m&mvi=3&pl=23&smhost=r3---sn-n8v7znsr.googlevideo.com&lsparams=hcs,mh,mm,mn,ms,mv,mvi,pl,smhost&lsig=AG3C_xAwRAIgEKE-o8ztsaAdjS0VG7V69PSUZCGzeXrwlcaTcOkmzTYCIB6j8J4KUooaoYfG7M4iqws2c67stqwN8BmiFAs5ejbz')
client.send_file('@py_hack06','https://r2---sn-b5an01-u5ne.googlevideo.com/videoplayback?expire=1638572788&ei=lE6qYdi0CoiYyQWT-rjQBw&ip=91.231.57.124&id=o-AOIanotPqLYvgh80R5OPcu8hHZJdhKBA_hVMzBCqDjje&itag=22&source=youtube&requiressl=yes&mh=Wz&mm=31%2C29&mn=sn-b5an01-u5ne%2Csn-ug5onuxaxjvh-n8vs&ms=au%2Crdu&mv=m&mvi=2&pl=23&initcwndbps=213750&vprv=1&mime=video%2Fmp4&ns=kJss-h4ax98wv373WEHAamkG&cnr=14&ratebypass=yes&dur=834.107&lmt=1638022259601350&mt=1638550873&fvip=2&fexp=24001373%2C24007246&c=WEB&txp=5535432&n=Hyu36glu_SY2enCxJs&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALjRa2kugYsHnhvKkWeLxUm8DlS04iTxQY5uZYKBKQDKAiEAjvD_CUYgCs6z2axWWNGXL6dqqa4kjgJMJAz1HmLxHbU%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAK8akqFaAHOV7ubA7NKr_2aCo0N1hzGkCiKTvoGyVC_WAiA6FDjVrgoGxbbDa2UQW0oKmIpqJ7scc_6d0ir7KEiBUw%3D%3D')
client.disconnect()
def main(argv):
    #file_path = argv[1]
    #file_name = argv[2]
    chat_id = argv[3]
    object_id = argv[4]
    bot_name = argv[5]
    duration = argv[6]
    mimetypes.add_type('audio/aac','.aac')
    mimetypes.add_type('audio/ogg','.ogg')
    msg = client.send_file(
                           413431533,
                           file_path,
                           caption=str(chat_id + ':' + object_id + ':' + duration),
                           file_name=str(file_name),
                           use_cache=False,
                           part_size_kb=512,
                           attributes=[DocumentAttributeAudio(
                                                      int(duration),
                                                      voice=None,
                                                      title=file_name[:-4],
                                                      performer='')]
                           )
    client.disconnect()
    return 0

if __name__ == '__main__':
    import sys
    #main(sys.argv[0:])
