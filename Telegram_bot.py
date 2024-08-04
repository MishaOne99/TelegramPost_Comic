"""Публикует по запросу пользователя случайный комикс"""

import os
import shutil
from Comic_Downloader import download_comics
from dotenv import load_dotenv
from telegram import Bot, InputMediaPhoto


COMIC_PATH = 'Comic/'
PNG_FORMAT = '.png'
DIRECTORY_NAME = 'Comic'


def publish_post(bot: dict, chat_id: str, image: str, coment: str) -> None:
    link_photo = f'{COMIC_PATH}{image}{PNG_FORMAT}'

    media_img = InputMediaPhoto(media = open(link_photo, 'rb'), caption=coment)

    bot.send_media_group(media=[media_img], chat_id=chat_id)


def publish_images_from_directory(token: str, chat_id: str) -> None:
    bot = Bot(token)
    
    comic_title, comic_comment = download_comics()
    
    publish_post(bot=bot, chat_id=chat_id, image=comic_title, coment=comic_comment)
    
    shutil.rmtree(DIRECTORY_NAME)


def main():
    """Запускает бота"""
    load_dotenv()
    
    token = os.environ['API_TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID_TELEGRAM']
    
    publish_images_from_directory(token=token, chat_id=chat_id)


if __name__ == '__main__':
    main()
