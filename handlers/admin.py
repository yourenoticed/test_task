from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database.requests import is_admin, get_admins, get_active_clients

admin_router = Router()


@admin_router.message(Command("admin"))
async def admin(message: Message):
    if await is_admin(message.chat.id):
        await message.answer("da, ty admin")
    else:
        await message.answer("snachala dorasti")
