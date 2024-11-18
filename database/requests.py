from database.models import User, Admin, Client, Menu, Order
from database.database import Base, engine, session
from sqlalchemy import select, join, insert


async def create_model():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_admins():
    async with session() as s:
        result = await s.scalars(select(Admin))
        return result.all()


async def is_admin(tg_id: int) -> bool:
    admins = await get_admins()
    for admin in admins:
        if admin.tg_id == tg_id:
            return True
    return False


async def add_user(user):
    async with engine.begin() as conn:
        await conn.execute(insert(User).values(
            [user[0], user[1], user[2]]
        ))


async def make_admin():
    async with engine.begin() as conn:
        await conn.execute(insert(Admin).values([460761422]))
