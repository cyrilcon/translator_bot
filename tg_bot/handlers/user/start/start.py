from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

command_start_router = Router()


@command_start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Это Telegram бот переводчик с русского на английский\n"
        "Введите текст на русском, чтобы бот перевёл его на английский язык"
    )
