"""Загрузка изображений в передаваемую директорию"""

from requests import get

def download_image(url: str, file_name: str, params: dict = None) -> None:
    """Загружает изображения

    Args:
        url (str): Ссылка на скачиваемое изображение
        file_name (str): Путь куда загружаются изображения
        params (dict, optional): Параметры передаваемые в get запрос. Defaults to None.
    """
    response = get(url, params)
    response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(response.content)
