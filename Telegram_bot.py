"""Публикует по запросу пользователя случайный комикс"""

import os
import shutil
from comic_downloader import download_random_comic
from dotenv import load_dotenv
from os import path
from pathlib import Path
from telegram import Bot, InputMediaPhoto


PNG_FORMAT = '.png'
DIRECTORY_NAME = 'Comic'


def publish_post(bot: dict, chat_id: str, image: int, coment: str) -> None:
    directory_path = path.join(DIRECTORY_NAME, str(image))
    link_photo = f'{directory_path}{PNG_FORMAT}'

    media_img = InputMediaPhoto(media = open(link_photo, 'rb'), caption=coment)

    bot.send_media_group(media=[media_img], chat_id=chat_id)


def publish_image_from_directory(token: str, chat_id: str) -> list:
    bot = Bot(token)
    
    comic_number, comic_comment = download_random_comic()
    
    post_publishing_details = [bot, chat_id, comic_number, comic_comment]
    
    return post_publishing_details


def main():
    """Запускает бота"""
    load_dotenv()
    token = os.environ['API_TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID_TELEGRAM']
    
    Path(DIRECTORY_NAME).mkdir(parents=True, exist_ok=True)
    
    try:
        post_publishing_details = publish_image_from_directory(token=token, chat_id=chat_id)
        publish_post(*post_publishing_details)
    finally:
        shutil.rmtree(DIRECTORY_NAME)


if __name__ == '__main__':
    main()
