# # from pytube import YouTube
# # #YouTube("https://www.youtube.com/watch?v=gpCIfQUbYlY").streams.first().download('/home/username/PycharmProjects/aiogram_u',"1.mp4")
# # #yt.download('/home/username/PycharmProjects/aiogram_u')
# # #https://www.youtube.com/watch?v=gpCIfQUbYlY
# #
# # def ok(qq,qe):
# #     print("OK")
# # #print(YouTube('https://www.youtube.com/watch?v=gpCIfQUbYlY').thumbnail_url)
# # yt=YouTube('https://www.youtube.com/watch?v=gpCIfQUbYlY',on_complete_callback=ok,)
# # #b=yt.streams.first().download('/home/username/PycharmProjects/aiogram_u',"my.mp4","2-")
# # b=yt.streams.get_highest_resolution().get_url()
# # print(b)
# #
# # #https://r4---sn-puppm01-u5ne.googlevideo.com/videoplayback?expire=1637508590&ei=jhGaYbmRLeiMv_IP-_COgAI&ip=92.38.55.105&id=o-AB-ny3BM9YF_7wqNBRKNVYoAmP9Mnj9yX7vlaPMo48fZ&itag=22&source=youtube&requiressl=yes&mh=p-&mm=31%2C29&mn=sn-puppm01-u5ne%2Csn-gvnuxaxjvh-n8vk&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=451250&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=1888.757&lmt=1634707822560064&mt=1637486683&fvip=4&fexp=24001373%2C24007246&c=ANDROID&txp=5311224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhALLFeeyHZbMLCnVMElsC74jpY_ChbpPPom9XemOCmHcDAiEAmgPyEgIuQNcvaJP1eXe4GckAIsiHMN-a0Ru0g37m1v8%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgUlLA_6Rgrpbx7xHEJTZpR8JP7YJfKrsi90bWr0SGG_gCIQCoRryVixvuqpEfdwshDwkffFEf3iyGkCllcX1IKCH5jA%3D%3D
# # #https://r4---sn-puppm01-u5ne.googlevideo.com/videoplayback?expire=1637508718&ei=DhKaYY_aCqL_yQW-yrWwBQ&ip=92.38.55.105&id=o-APm_2h_rwh-VX8omSBNA61MkeqngJITCr3dyEBhsCGyY&itag=17&source=youtube&requiressl=yes&mh=p-&mm=31%2C29&mn=sn-puppm01-u5ne%2Csn-gvnuxaxjvh-n8vk&ms=au%2Crdu&mv=m&mvi=4&pl=22&initcwndbps=451250&vprv=1&mime=video%2F3gpp&gir=yes&clen=10837283&dur=1888.803&lmt=1634683621033830&mt=1637486683&fvip=4&fexp=24001373%2C24007246&c=ANDROID&txp=6211224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAN9rFrUtLLYDzSg4H4XyH8hVVPnAqlDhWiF08Qgw1HO6AiAIdKqw003EmC4TYvvP3sgBuh9HBNi4nSFkvpOTWGX68g%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgPr4G3_JPxCA6eYODu7L2e41CLODTgcWmtH7Gem68a1YCICEzSBIV9rOE5e8cFL7P4WLHszKQq5cA5e_oGbwq5a_2
# #
#
# ##<video style="width: 853px; height: 480px; left: 250px; top: 0px;" tabindex="-1" class="video-stream html5-main-video" controlslist="nodownload" src="blob:https://www.youtube.com/3c87a63a-2c42-4c1c-99b3-14ba453860d8"></video>
#
#
# fromurl = 'https://www.youtube.com/watch?v=usP1arGSVGQ',
# import youtube_dl
#
# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
#
# with ydl:
#     result = ydl.extract_info(
#         'https://www.youtube.com/watch?v=usP1arGSVGQ',
#         download=False # We just want to extract the info
#     )
#
# if 'entries' in result:
#     # Can be a playlist or a list of videos
#     video = result['entries'][0]
# else:
#     # Just a video
#     video = result
#
# #print(video)
# video_url = video['formats']
# total=None
# for i in video_url:
#     print(i)
#     print("--------------------------------------------")
#     if i['format_note']=='720p':
#         total=i['url']
#
# print(total)


x='qssq'
y=456
z='dqdx'
t=[x,str(y),z]
print(' '.join(t))
text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# join elements of text with space
print(' '.join(text))