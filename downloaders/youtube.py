import aiogram
import pytube

from settings import logger
from handlers.keyboard import FSMAdmin
from pytube import  YouTube,Playlist
from aiogram import types, Dispatcher
from data_base.work_with_db import *
from create_bot import bot
import send_from_user
import os
import moviepy.editor as mp

class Youtube:
    def __init__(self,link,type,message:types.Message):
        self.size=None
        self.quality=None
        self.video_name=None
        self.fps=None
        self.video_type=type
        self.link_type=None
        self.is_true=None
        self.first_link=link
        self.link=None
        self.message=message
        try:
            YouTube(self.first_link)
            self.link_type='Video'
        except:
            try:
                Playlist(self.first_link)
                self.link_type='PlayList'
            except:
                self.is_true=0
    @logger.catch()
    async def youtube_video(self):
        video=None
        logger.debug(self.first_link)
        yt=YouTube(self.first_link)
        if self.video_type=="Аудио":
            video=yt.streams.get_lowest_resolution()
        elif self.video_type=="Видео":
            video=yt.streams.get_highest_resolution()

        self.size = video.filesize
        self.quality = video.resolution
        self.video_name = video.title
        self.fps = str(video.fps)
        logger.debug(f"Size: {str(self.size)}B({str(int(self.size)/1024/1024)}MB), quality: {self.quality}, videos name: {self.video_name}, fps: {str(self.fps)}")

        if (int(self.size) / 1024 / 1024) < 370:
            file_id = check_youtube_video(self.video_name, self.quality, self.fps)
            logger.debug(file_id)
            logger.debug(f"File id: {file_id}")
            if str(file_id) == '0':
                logger.debug("Downloading youtube video")
                a = await bot.send_message(self.message.from_user.id,"Видео(аудио) скачивается на сервер...")
                path = video.download()
                clip = mp.VideoFileClip(path)
                clip.audio.write_audiofile("theaudio.mp3")
                await bot.edit_message_text(f"Видео отпправляется.\nОжидайте",self.message.from_user.id,a.message_id)
                logger.debug("Downloaded!")
                await send_from_user.send_vf('theaudio.mp3', self.message, str(self.size), self.quality, self.video_name, self.fps,self.video_type)
                await bot.delete_message(self.message.from_user.id,a.message_id)
                os.remove(path)
                os.remove('theaudio.mp3')
            elif str(file_id) == "Error":
                await bot.send_message(self.message.from_user.id, 'Произошла ошибка!')
            else:
                try:
                    if self.video_type=="Видео":
                        await bot.send_video(self.message.from_user.id, file_id[0], caption=self.video_name)
                    elif self.video_type=="Аудио":
                        await bot.send_audio(self.message.from_user.id,file_id[0],caption=self.video_name)

                except aiogram.utils.exceptions.WrongFileIdentifier:
                    logger.info(f"File id {file_id[0]} is old?")
                    youtube_videos_delete(self.video_name,self.quality,self.fps)
                    # await youtube(message,url)
        else:
            await bot.send_message(message.from_user.id, 'Размер видео больше чем 370МБ(техническое ограничение)')
            return "not Found"

    async def youtube_playlist(message:types.Message,yt,state):
        pass

    async def send_video(self):
        if self.link_type=='Video':
            await self.youtube_video()