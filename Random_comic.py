"""Возвращает случайный комикс из заготовленной директории"""

import os
from random import shuffle, randint

DIRECTORY_NAME = 'Comics'
PATH = 'Comics/Coments.txt'


def returns_random_comic():
    """Возвращает случайный комикс и описание к нему
    """
    comics = os.listdir(DIRECTORY_NAME)[1:]
    shuffle(comics)
    count_comics = len(comics)

    comic = (comics[randint(0, count_comics)])
    
    with open(PATH, 'r') as file:
        comments = file.readlines()
        
    comment = {x[0:3].rstrip(' :'):x for x in comments}
    
    return comic, comment[comic[1:3].rstrip()][3:].lstrip(' :')


returns_random_comic()