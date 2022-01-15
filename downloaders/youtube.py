import os

import settings

import aiogram
import moviepy.editor as mp
from aiogram import types
from pytube import YouTube, Playlist

import send_from_user
from create_bot import bot
from data_base.work_with_db import *


class Youtube:
    def __init__(self, link, type, message: types.Message):
        self.size = None
        self.quality = None
        self.video_name = None
        self.fps = None
        self.video_type = type#видео надо доставить в ввиде аудио либо видео
        self.link_type = None#т.е first_link эти url видео или плэй листа
        self.is_true = None#видео вообще существует?
        self.video_link = None#нужен во время скачивания видео
        #-------------------------------------------------------изменяю
        self.first_link = link #нужен для проверки типа url
        self.pl_link=None#url плэй листа, что бы не потерять
        self.message = message
        self.continue_downloading=1#0# нужен для кнопки отмена при скачивании плэй- листа к примеру посло тего, как скачал одно видео и хочешь остановаить
        try:
            YouTube(self.first_link)
            self.link_type = 'Video'
            self.video_link=link
            logger.debug("Video")
        except:
            try:
                Playlist(self.first_link)
                self.link_type = 'PlayList'
                self.pl_link=link
                logger.debug("PlayList")
            except:
                self.is_true = 0

    @logger.catch()
    async def youtube_video(self,link=None):
        logger.info(link)
        if link!=None:
            self.video_link=link
        video = None
        logger.debug(self.video_link)
        yt = YouTube(self.video_link)
        if self.video_type == "Аудио":
            video = yt.streams.get_audio_only('mp4')
        elif self.video_type == "Видео":
            video = yt.streams.get_highest_resolution()

        self.size = video.filesize
        self.quality = video.resolution
        self.video_name = video.title
        try:
            self.fps = str(video.fps)
        except AttributeError:
            self.fps = 'None'
        if self.quality == None:
            self.quality = 'None'
        logger.debug(
            f"Size: {str(self.size)}B({str(int(self.size) / 1024 / 1024)}MB), quality: {self.quality}, videos name: {self.video_name}, fps: {str(self.fps)}")

        if (int(self.size) / 1024 / 1024) < 370:
            file_id = check_youtube_video(self.video_name, self.quality, self.fps)
            logger.debug(file_id)
            logger.debug(f"File id: {file_id}")
            if str(file_id) == '0':
                logger.debug("Downloading youtube video")
                a = await bot.send_message(self.message.from_user.id, f"{self.video_type} скачивается на сервер...")
                path = video.download()
                if self.video_type == "Аудио":
                    mp4_without_frames = mp.AudioFileClip(path)
                    mp4_without_frames.write_audiofile('themusic.mp3')
                    mp4_without_frames.close()
                await bot.edit_message_text(f"{self.video_type} отправляется.\nОжидайте", self.message.from_user.id, a.message_id)
                logger.debug("Downloaded!")
                if self.video_type=="Аудио":
                    await send_from_user.send_vf('themusic.mp3', self.message, str(self.size), self.quality,
                                                self.video_name, self.fps, self.video_type)
                else:
                    await send_from_user.send_vf(path, self.message, str(self.size), self.quality,
                                                 self.video_name, self.fps, self.video_type)
                await bot.delete_message(self.message.from_user.id, a.message_id)
                os.remove(path)
                if self.video_type=="Аудио":
                    os.remove('themusic.mp3')
            elif str(file_id) == "Error":
                await bot.send_message(self.message.from_user.id, 'Произошла ошибка!')
            else:
                try:
                    if self.video_type == "Видео":
                        await bot.send_video(self.message.from_user.id, file_id[0], caption=self.video_name)
                    elif self.video_type == "Аудио":
                        await bot.send_voice(self.message.from_user.id, file_id[0], caption=self.video_name)

                except aiogram.utils.exceptions.WrongFileIdentifier:
                    logger.info(f"File id {file_id[0]} is old?")
                    youtube_videos_delete(self.video_name, self.quality, self.fps)
                    await self.youtube_video()
        else:
            await bot.send_message(self.message.from_user.id, 'Размер видео больше чем 370МБ(техническое ограничение)')
            return "not Found"

    async def youtube_playlist(self):
        pl=Playlist(self.pl_link)
        logger.debug(settings.state_of_keyboard)
        for i in pl.video_urls:
            if settings.state_of_keyboard == 'YouTube':
                await self.youtube_video(i)


    async def send_video_youtube(self):
        logger.debug(self.link_type)
        if self.link_type == 'Video':
            await self.youtube_video()
        elif self.link_type=='PlayList':
            await self.youtube_playlist()
