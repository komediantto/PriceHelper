import os

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType

from config.loader import config
from constants import main as phrases
from keyboards import main
from states.cost import Settings, Sum


async def settings(message: types.Message, state: FSMContext):
    if message.from_user.id == config.tg_bot.admin_id:
        await message.reply("Введите новое значение для rate:")
        await state.set_state(Settings.waiting_for_rate)

    else:
        await message.reply("У вас нет доступа к этой команде.")


async def change_rate(message: types.Message, state: FSMContext):

    if message.content_type == ContentType.TEXT:
        try:
            new_rate = float(message.text)
            phrases.RATE = new_rate
            await state.update_data(rate=new_rate)
            await message.reply(f"Новое значение rate установлено: {new_rate}")
            await state.finish()
        except ValueError:
            await message.reply("Введите корректное значение rate (целое число).")
    else:
        await message.reply("Введите корректное значение rate (целое число).")


async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(phrases.WELCOME, reply_markup=main.start_kb())


async def pre_calculation(message: types.Message, state: FSMContext):
    await message.answer(phrases.CHOOSE, reply_markup=main.categories())
    await state.set_state(Sum.choose)


async def reviews(message: types.Message,):
    await message.answer(phrases.REVIEWS)


async def answers(message: types.Message,):
    await message.answer(phrases.ANSWERS)


async def exchange(message: types.Message,):
    photo_path = os.path.join('pictures', 'picture2.png')

    with open(photo_path, "rb") as photo_file:
        await message.answer_photo(photo=types.InputFile(photo_file),
                                   caption=phrases.EXCHANGE.format(rate=phrases.RATE))


async def connect(message: types.Message,):
    await message.answer(phrases.CONNECT)


async def back(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(phrases.WELCOME, reply_markup=main.start_kb())


def register(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"], state="*")
    dp.register_message_handler(settings, Command("settings"))
    dp.register_message_handler(change_rate, content_types=ContentType.TEXT,
                                state=Settings.waiting_for_rate)
    dp.register_message_handler(pre_calculation, text='Рассчитать стоимость 📲')
    dp.register_message_handler(reviews, text='Отзывы 📝')
    dp.register_message_handler(answers, text='Ответы на все вопросы 🔮')
    dp.register_message_handler(exchange, text='Актуальный курс💹')
    dp.register_message_handler(connect, text='Связаться с оператором 👀')
    dp.register_message_handler(back, text='Назад', state=Sum.choose)
