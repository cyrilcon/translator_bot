from aiogram import Router
from aiogram.types import Message

unprocessed_messages_router = Router()


@unprocessed_messages_router.message()
async def unprocessed_messages(message: Message):
    await message.answer(
        "Нераспознанное сообщение 😕\n"
        "Введите текст на русском, чтобы бот перевёл его на английский язык"
    )
