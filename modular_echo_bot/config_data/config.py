#from dataclasses import dataclass
#from environs import Env
#
#@dataclass
#class TgBot:
#    token: str
#
#@dataclass
#class Config:
#    tg_bot: TgBot
#
#def load_config(path: str | None = None) -> Config:
#    env = Env()
#    env.read_env(path)
#    return Config(tf_bot = TgBot(tokenenv=env('BOT_TOKEN')))
#
#if __name__ == "__main__":
#    config = load_config()  # Сначала загружаем конфиг
#    print("Токен:", config.tg_bot.token)  # Обращаемся к экземпляру, а не классу

from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str  # Обратите внимание - поле называется 'token'

@dataclass
class Config:
    tg_bot: TgBot  # Поле называется 'tg_bot' (не tf_bot!)

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))  # Все имена полей теперь согласованы

if __name__ == "__main__":
    try:
        config = load_config()
        print("Токен успешно загружен:", config.tg_bot.token)
    except Exception as e:
        print(f"Ошибка загрузки конфига: {e}")