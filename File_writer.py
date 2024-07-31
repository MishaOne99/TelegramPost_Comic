"""Создание файла и запись в него текста"""

PATH = 'Comics/'
FILE_NAME = 'Coments.txt'

def save_comment(comic_num: int, comic_comment: str) -> None:
    """Создаёт файл и записывает в него полученную информацию 

    Args:
        comic_num (int): Номер комикса
        comic_comment (str): Комментарий к комиксу
    """
    with open(f'{PATH}{FILE_NAME}', 'a') as file:
        file.write(f'{comic_num} : {comic_comment}\n')