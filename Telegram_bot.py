"""Публикует по запросу пользователя случайный комикс"""

import os
from dotenv import load_dotenv
from Random_comic import returns_random_comic
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup
from pathlib import Path


PATH = 'Comics/'

load_dotenv()
token = os.environ['API_TELEGRAM_TOKEN']
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def display_welcome_screen(message):
    """Выводит приветствие

    Args:
        message (_type_): _description_
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Вывести случайный комикс')
    text = 'Приветствую тебя 👋🏻'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Вывести случайный комикс')
def random_output_comics(message):
    """Выводит случайный комикс и удаляет его с компьютера

    Args:
        message (_type_): _description_
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Вывести случайный комикс')
    comic, comment = returns_random_comic()
    comic_path = f'{PATH}{comic}'
    
    bot.send_photo(message.chat.id, open(comic_path, 'rb'))
    Path.unlink(comic_path)
    bot.send_message(message.chat.id, comment, reply_markup=markup)


def main():
    """Запускает бота"""
    bot.infinity_polling()


if __name__ == '__main__':
    main()