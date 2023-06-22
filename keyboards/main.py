from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           ReplyKeyboardMarkup)
from aiogram.utils.callback_data import CallbackData
from constants.main import CATEGORIES, START

callback_clothes = CallbackData('clothes', 'fee', 'china', 'chmos')

back = InlineKeyboardButton(text='Назад', callback_data='back')


def start_kb():
    kb = ReplyKeyboardMarkup(row_width=2)
    buttons = []
    for item in START:
        button = item[0]
        buttons.append(button)
    kb.add(*buttons)
    return kb


def categories():
    kb = ReplyKeyboardMarkup(row_width=2)
    b1 = CATEGORIES['shoes']
    b2 = CATEGORIES['hoodie']
    b3 = CATEGORIES['t-shirt']
    b4 = CATEGORIES['socks']
    b5 = 'Назад'
    kb.add(*[b1, b2, b3, b4, b5])
    return kb
