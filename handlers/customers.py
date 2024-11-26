from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from database.requests import add_user
from service import get_user_info
from handlers.keyboards import main_kbr

clients_router = Router()


@clients_router.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Здравствуй, клиентик", reply_markup=main_kbr)
    await add_user(get_user_info(message))


@clients_router.message(F.text == "Меню")
async def menu(message: Message):
    await message.reply("Это меню")


@clients_router.message(F.text == "Мои заказы")
async def menu(message: Message):
    await message.reply("Это твои заказы")
