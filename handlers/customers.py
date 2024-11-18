from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from database.requests import get_admins, add_user, is_admin
from service import get_user_info

customers_router = Router()


@customers_router.message(CommandStart())
async def start(message: Message):
    await add_user(get_user_info(message))
    await message.answer("fuck you")


@customers_router.message(Command("admin"))
async def admin(message: Message):
    if await is_admin(message.chat.id):
        await message.answer("da, ty admin")
    else:
        await message.answer("snachala dorosti")
