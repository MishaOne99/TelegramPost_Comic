'''Создаёт директорию в файловой системе и скачивает в неё фотографии комиксов с их комментариями'''

from download_image import download_image
from os import path
from random import randint
from requests import get
from urllib.parse import SplitResult


DIRECTORY_NAME = 'Comic'
PNG_FORMAT = '.png'
COMIC_NAME = 'info.0.json'
    
    
def get_comic_count() -> int:
    """Узнаёт номер последнего комикса

    Returns:
        int: Номер последнего комикса, является количеством комиксов
    """
    responce = get('https://xkcd.com/info.0.json')
    responce.raise_for_status()
    
    comic_count = responce.json()['num']
    
    return comic_count


def download_random_comic() -> list:
    """Скачивает случайный комикс
    """
    comic_count = get_comic_count()
    comic_number = randint(0, comic_count)

    url = SplitResult(scheme='https', netloc='xkcd.com', path=f'/{comic_number}/{COMIC_NAME}', query=None, fragment=None)

    responce = get(url.geturl())
    responce.raise_for_status()

    comic_info = responce.json()
    comic_url = comic_info['img']
    comic_comment = comic_info['alt']
    
    directory_path = path.join(DIRECTORY_NAME, str(comic_number))

    file_name = f'{directory_path}{PNG_FORMAT}'

    download_image(url=comic_url, file_name=file_name)
    
    return [comic_number, comic_comment]
