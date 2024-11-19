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
    async with session() as s:
        result = await s.scalar(select(Admin).where(Admin.tg_id == tg_id))
        if result:
            return True
        return False


async def add_user(user: list) -> None:
    async with engine.begin() as conn:
        await conn.execute(insert(User).values(user))


async def make_admin(tg_id: int) -> None:
    async with engine.begin() as conn:
        await conn.execute(insert(Admin).values([tg_id]))
