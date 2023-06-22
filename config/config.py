import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class Config:
    tg_bot: TgBot


def load_config() -> Config:
    return Config(tg_bot=TgBot(token=os.getenv('BOT_TOKEN'), admin_id=int(os.getenv('ADMIN_ID'))))
