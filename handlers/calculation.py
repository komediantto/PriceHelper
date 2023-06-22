from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from loguru import logger

from constants import main as phrases
from keyboards import main
from states.cost import Sum
import os


async def calculation_shoes(message: types.Message,
                            state: FSMContext):
    await state.update_data(fee=2400,
                            china=300,
                            chmos=1100)
    photo_path = os.path.join('pictures', 'picture.png')
    with open(photo_path, "rb") as photo_file:
        await message.answer_photo(photo=types.InputFile(photo_file),
                                   caption=phrases.GET_SUM)
    await state.set_state(Sum.cost_shoes)


async def calculation_hoodie(message: types.Message,
                             state: FSMContext):
    await state.update_data(fee=2000,
                            china=250,
                            chmos=750)
    photo_path = os.path.join('pictures', 'picture.png')
    with open(photo_path, "rb") as photo_file:
        await message.answer_photo(photo=types.InputFile(photo_file),
                                   caption=phrases.GET_SUM)
    await state.set_state(Sum.cost_hoodie)


async def calculation_t_shirt(message: types.Message,
                              state: FSMContext):
    await state.update_data(fee=1750,
                            china=250,
                            chmos=500)
    photo_path = os.path.join('pictures', 'picture.png')
    with open(photo_path, "rb") as photo_file:
        await message.answer_photo(photo=types.InputFile(photo_file),
                                   caption=phrases.GET_SUM)
    await state.set_state(Sum.cost_t_shirt)


async def calculation_socks(message: types.Message,
                            state: FSMContext):
    await state.update_data(fee=1600,
                            china=200,
                            chmos=400)
    photo_path = os.path.join('pictures', 'picture.png')
    with open(photo_path, "rb") as photo_file:
        await message.answer_photo(photo=types.InputFile(photo_file),
                                   caption=phrases.GET_SUM)
    await state.set_state(Sum.cost_socks)


async def get_sum(message: types.Message, state: FSMContext):

    data = await state.get_data()
    try:
        cost = float(message.text)
    except ValueError:
        await message.answer('Введите число')
        return
    rate = data.get("rate", phrases.RATE)
    calc = (cost * phrases.RATE) + int(data['fee'])
    await message.answer(phrases.ITOGO.format(calc=round(calc), rate=rate))
    await message.answer(phrases.SECOND, reply_markup=main.categories())
    await state.set_state(Sum.choose)


def register(dp: Dispatcher):
    dp.register_message_handler(calculation_shoes, text='Обувь/Верхняя одежда 👟',
                                state=[Sum.choose,
                                       Sum.cost_shoes,
                                       Sum.cost_hoodie,
                                       Sum.cost_t_shirt,
                                       Sum.cost_socks])
    dp.register_message_handler(calculation_hoodie, text='Толстовки/Штаны 👘',
                                state=[Sum.choose,
                                       Sum.cost_shoes,
                                       Sum.cost_hoodie,
                                       Sum.cost_t_shirt,
                                       Sum.cost_socks])
    dp.register_message_handler(calculation_t_shirt, text='Футболка/Шорты 👕',
                                state=[Sum.choose,
                                       Sum.cost_shoes,
                                       Sum.cost_hoodie,
                                       Sum.cost_t_shirt,
                                       Sum.cost_socks])
    dp.register_message_handler(calculation_socks, text='Носки/Нижнее белье 🧦',
                                state=[Sum.choose,
                                       Sum.cost_shoes,
                                       Sum.cost_hoodie,
                                       Sum.cost_t_shirt,
                                       Sum.cost_socks])
    dp.register_message_handler(get_sum, state=[Sum.choose,
                                                Sum.cost_shoes,
                                                Sum.cost_hoodie,
                                                Sum.cost_t_shirt,
                                                Sum.cost_socks])
