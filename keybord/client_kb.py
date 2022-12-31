from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bt1 = KeyboardButton('🗂 Каталог товаров')
bt2 = KeyboardButton('❓ Информация')
bt3 = KeyboardButton('🆘 Помощь')
bt4 = KeyboardButton('🛒 Корзина')
bt5 = KeyboardButton('🛒 Корзина')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(bt1, bt2)\
    .add(bt3).add(bt4)
