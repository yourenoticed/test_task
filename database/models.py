from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base


class User(Base):
    __tablename__ = "users"
    tg_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    phone_number: Mapped[str | None]


class Admin(Base):
    __tablename__ = "admins"
    tg_id: Mapped[int] = mapped_column(
        ForeignKey("users.tg_id"), primary_key=True)


class Client(Base):
    __tablename__ = "clients"
    tg_id: Mapped[int] = mapped_column(
        ForeignKey("users.tg_id"), primary_key=True)
    orders_amount: Mapped[int]


class Menu(Base):
    __tablename__ = "menu"
    item_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]


class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(ForeignKey("clients.tg_id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("menu.item_id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    finished_at: Mapped[datetime | None]
    canceled: Mapped[bool] = mapped_column(default=False)
