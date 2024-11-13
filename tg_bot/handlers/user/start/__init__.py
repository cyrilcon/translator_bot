__all__ = ("start_routers",)

from aiogram import Router

from .start import command_start_router

start_routers = Router()
start_routers.include_routers(
    command_start_router,
)
