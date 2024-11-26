from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


main_kbr = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню")],
    # [KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Мои заказы")]],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт"
)
