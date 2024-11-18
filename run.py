from os import environ
from asyncio import run
from aiogram import Bot, Dispatcher
from handlers.customers import customers_router
from handlers.admin import admin_router
from database.requests import create_model, make_admin


async def main():
    bot = Bot(environ.get("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(customers_router, admin_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())
