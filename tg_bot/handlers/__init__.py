__all__ = ("routers",)

from aiogram import Router

from .user import user_routers

routers = Router()
routers.include_routers(
    user_routers,
)
