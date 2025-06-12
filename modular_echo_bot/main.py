import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

# Инициализируем логгер
logger = logging.getLogger(__name__)
# Функция конфигурирования и зупаска бота
async def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='{filename}:{lineno} #{levelname:<8} [{asctime}] - {name} - {message}',
        style='{'
    )
    logger.debug('Starting bot')

    config: Config = load_config()
    token = config.tg_bot.token.strip()  # Очистка токена

    bot = Bot(token=token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())