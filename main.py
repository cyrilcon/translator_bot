import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import AiogramError
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from tg_bot.handlers import routers
from tg_bot.services import set_default_commands, set_bot_description

from config import config


async def on_startup(bot: Bot):
    """
    Called on bot startup.
    """

    await set_default_commands(bot)
    await set_bot_description(bot)

    try:
        await bot.send_message(chat_id=config.admin, text="Bot restarted!!")
    except AiogramError:
        pass


async def on_shutdown():
    """
    Called on bot shutdown.
    """

    pass


def setup_logging():
    """
    Set up logging configuration for the application.
    """

    log_level = config.logging_level
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=log_level,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting the bot")


def get_storage():
    """
    Return storage based on the provided configuration.

    Returns:
        Storage: The storage object based on the configuration.
    """

    return MemoryStorage()


async def main():
    setup_logging()  # Set logging

    storage = get_storage()

    bot = Bot(
        token=config.token,
        default=DefaultBotProperties(parse_mode="HTML"),
    )
    dp = Dispatcher(
        storage=storage,
        fsm_strategy=FSMStrategy.CHAT,  # CHAT - state and data common for the whole chat
    )

    dp.include_routers(routers)  # Installing routers

    await on_startup(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await on_shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Stopping the bot")
