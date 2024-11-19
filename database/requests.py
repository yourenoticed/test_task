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


async def get_menu_items() -> list[Menu]:
    async with session() as s:
        result = await s.scalars(select(Menu))
        return result.all()


async def get_clients() -> list[Client]:
    async with session() as s:
        result = await s.scalars(select(Client))
        return result.all()


async def get_active_orders() -> list[Order]:
    async with session() as s:
        result = await s.scalars(select(Order).where(Order.finished_at == None))
        return result.all()


async def get_finished_orders() -> list[Order]:
    async with session() as s:
        result = await s.scalars(select(Order).where(Order.finished_at != None, Order.canceled == False))
        return result.all()


async def get_canceled_orders() -> list[Order]:
    async with session() as s:
        result = await s.scalars(select(Order).where(Order.canceled == True))
        return result.all()


# I think I can come up with a better solution for these two functions
async def get_active_clients() -> list[Client]:
    active_clients_id = {order.tg_id for order in await get_active_orders()}
    clients = await get_clients()
    active_clients = [
        client for client in clients if client.tg_id in active_clients_id]
    return active_clients


async def get_unactive_clients() -> list[Client]:
    active_clients_id = {order.tg_id for order in await get_active_orders()}
    clients = await get_clients()
    unactive_clients = [
        client for client in clients if client.tg_id not in active_clients_id]
    return unactive_clients
