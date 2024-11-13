from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionMiddleware

from tg_bot.services import translate_text

translate_router = Router()
translate_router.message.middleware(ChatActionMiddleware())


@translate_router.message(F.text, flags={"chat_action": "typing"})
async def translate(message: Message):
    translated_text = await translate_text(message.text)
    await message.answer(translated_text)
