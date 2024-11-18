from aiogram.types import Message
from database.models import User


def get_user_info(message: Message):
    tg_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    return (tg_id, first_name, last_name)
