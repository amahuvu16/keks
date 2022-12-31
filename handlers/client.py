import types
import pathlib
import sys
from data_base import Sql_baza as sql
from aiogram import Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
from keybord import client_kb
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMClient(StatesGroup):
    area_name = State()
    id_product = State()
    count_prod = State()

async def start(message: Message):
    try:
        sti = open(pathlib.Path(sys.argv[0]).parent / 'photo/start.jpg', 'rb')
        sql.chek_user_in_bd(message.from_user.id, message.from_user.first_name)
        await  bot.send_photo(message.chat.id, sti, f"""Здравствуйте {message.from_user.first_name}.\n
Меня зовут Оля и это мой магазинчик сладостей @OlyaMinicake_shop_bot.
Здесь вы можете просмотреть весь асортимент
и выбрать то что вам понравиться.\n

Данное приложение разработано @joneastofurik""",reply_markup=client_kb.main_menu)
    #     await bot.send_message(message.from_user.id, f"""Приветствую {message.from_user.first_name}.\n
    # Актуальные новости тут https://t.me/+03gJjlQJnfozMzYy""", reply_markup=client_kb.client_case_button)
    except Exception as err:
        print(err)
        await bot.send_message(message.chat.id, f'🚫 | Ошибка при выполнении команды')

async def catalog(message: Message):
    try:
        await FSMClient.area_name.set()
        await bot.send_message(message.chat.id, 'Представлены все виды десертов')#,reply_markup= )
    except:
        await bot.send_message(message.chat.id, f'🚫 | Ошибка при выполнении команды')

async def calendar_check(message: Message):
    calendar, step = DetailedTelegramCalendar().build()
    await bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)
    # print(DetailedTelegramCalendar().build())

@dp.callback_query_handler(DetailedTelegramCalendar().func())
async def cal(call: CallbackQuery):
    result, key, step = DetailedTelegramCalendar().process(call.data)
    if not result and key:
        await bot.edit_message_text(f"Select {LSTEP[step]}",
                                  call.message.chat.id,
                                  call.message.message_id,
                                  reply_markup=key)
    elif result:
        await bot.edit_message_text(f"You selected {result}",
                                  call.message.chat.id,
                                  call.message.message_id)


# async def overed(message: Message):
#     try:
#         await bot.send_message(message.from_user.id, 'sgl')
#     except:
#         print('overed')

def register_handlers_clients(dp : Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(calendar_check, commands='calendar')
    dp.register_message_handler(catalog, lambda message: message.text == '🗂 Каталог товаров', state=None)
    # dp.register_message_handler(overed, content_types='text')