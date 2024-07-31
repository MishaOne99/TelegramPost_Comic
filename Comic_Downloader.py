'''Создаёт директорию в файловой системе и скачивает в неё фотографии комиксов с их комментариями'''

import argparse
from Download_image import download_image
from File_writer import save_comment
from pathlib import Path
from requests import get
from urllib.parse import SplitResult


DIRECTORY_NAME = 'Comics'
PATH = 'Comics/'
PNG_FORMAT = '.png'
COMIC_NAME = 'info.0.json'
    
    
def download_comics(comics_count: int) -> None:
    """Создание директории и загрузка в неё данных

    Args:
        comics_count (int): Количество загружаеммых комиксов
    """    
    Path(DIRECTORY_NAME).mkdir(parents=True, exist_ok=True)

    for comic_index in range(1, comics_count+1):
        url = SplitResult(scheme='https', netloc='xkcd.com', path=f'/{comic_index}/{COMIC_NAME}', query=None, fragment=None)

        responce = get(url.geturl())
        responce.raise_for_status()

        comic_info = responce.json()
        comic_url = comic_info['img']
        comic_number = comic_info['num']
        comic_title = comic_info['title']
        comic_comment = comic_info['alt']

        file_name = f'{PATH}№{comic_number} - {comic_title}{PNG_FORMAT}'

        download_image(url=comic_url, file_name=file_name)
        save_comment(comic_num=comic_number, comic_comment=comic_comment)


def main():
    """Позволяет работать из командной строки
    """
    parser = argparse.ArgumentParser(description= 'Downloads xkcd comics')
    parser.add_argument('Total_Downloaded_Comics', type=int, nargs='?', default=1, help='Enter the number of comics you want to download')
    args = parser.parse_args()

    comics_count = args.Total_Downloaded_Comics
    download_comics(comics_count=comics_count)


if __name__ == '__main__':
    main()