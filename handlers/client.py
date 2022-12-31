from aiogram import Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP


async def start(message: Message):
    # calendar, step = DetailedTelegramCalendar().middle_button_month.
    # await bot.send_message(message.chat.id, f"Select {LSTEP[step]}", reply_markup=calendar)
    print(DetailedTelegramCalendar().build())

async def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        await bot.edit_message_text(f"Select {LSTEP[step]}",
                                  c.message.chat.id,
                                  c.message.message_id,
                                  reply_markup=key)
    elif result:
        await bot.edit_message_text(f"You selected {result}",
                                  c.message.chat.id,
                                  c.message.message_id)
    # try:
    #     sti = open('start.webp', 'rb')
    #     await bot.send_sticker(message.from_user.id, sti)
    #     sql.chek_user_in_bd(message.from_user.id, message.from_user.first_name)
    #     # if sql.get_access(uid)[0]==777 or sql.get_access(uid)[0]==1:
    #     # markup.add(bt5,bt6,bt7)
    #
    #     await bot.send_message(message.from_user.id, f"""Приветствую {message.from_user.first_name}.\n
    # Актуальные новости тут https://t.me/+03gJjlQJnfozMzYy""", reply_markup=client_kb.client_case_button)
    # except Exception as err:
    #     print(err)
    #     await bot.send_message(message.chat.id, f'🚫 | Ошибка при выполнении команды')

# async def overed(message: Message):
#     try:
#         await bot.send_message(message.from_user.id, 'sgl')
#     except:
#         print('overed')

def register_handlers_clients(dp : Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.callback_query_handler(func=DetailedTelegramCalendar.func())
    # dp.register_message_handler(overed, content_types='text')