from aiogram.dispatcher.filters.state import State, StatesGroup


class Sum(StatesGroup):
    waiting = State()
    choose = State()
    cost_shoes = State()
    cost_hoodie = State()
    cost_t_shirt = State()
    cost_socks = State()
    test = State()


class Settings(StatesGroup):
    waiting_for_rate = State()
