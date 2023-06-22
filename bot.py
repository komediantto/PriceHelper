from aiogram.utils import executor

from config.loader import dp
from handlers import main, calculation

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

dp.middleware.setup(LifetimeControllerMiddleware())

main.register(dp=dp)
calculation.register(dp=dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
