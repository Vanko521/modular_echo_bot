import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

# Инициализируем логгер
logger = logging.getLogger(__name__)
# Функция конфигурирования и зупаска бота
async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
    level=logging.DEBUG,
    format='{filename}:{lineno} #{levelname:<8} [{asctime}] - {name} - {message}',
    style='{'
                       )
    # Выводим в консоль информацию о начале запуска бота
    logger.debug('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token = config.tg_bot.token)
    dp = Dispatcher()

    # Пропускаем накопившеися апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_poling(bot)

asyncio.run(main())