from aiogram import Bot


async def set_bot_description(bot: Bot):
    """
    Set bot description.

    :param bot: Bot instance to set description.
    """

    await set_short_description(bot)
    await bot.set_my_description("Telegram бот переводчик с русского на английский")


async def set_short_description(bot: Bot):
    """
    Set bot short description.

    :param bot: Bot instance to set description.
    """

    await bot.set_my_short_description("Telegram бот переводчик с русского на английский")
