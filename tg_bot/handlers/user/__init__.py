__all__ = ("user_routers",)

from aiogram import Router

from .start import start_routers
from .translate import translate_routers
from .unprocessed_messages import unprocessed_messages_router

user_routers = Router()
user_routers.include_routers(
    start_routers,
    translate_routers,
    unprocessed_messages_router,
)
