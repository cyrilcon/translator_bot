from typing import List

from aiogram import Bot, types


def get_commands() -> List[types.BotCommand]:
    """
    Generate list of bot commands based on user role.

    :return: List of BotCommand objects.
    """

    commands = [
        types.BotCommand(
            command="start",
            description="🔄 Перезагрузить бота",
        ),
    ]
    return commands


async def set_default_commands(bot: Bot):
    """
    Set bot commands for different languages and roles.

    :param bot: Bot instance to set commands for.
    """

    await bot.set_my_commands(get_commands())
