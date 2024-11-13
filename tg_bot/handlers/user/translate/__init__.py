__all__ = ("translate_routers",)

from aiogram import Router

from .translate import translate_router

translate_routers = Router()
translate_routers.include_routers(
    translate_router,
)
