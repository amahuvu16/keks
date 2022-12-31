from aiogram import types, Dispatcher



async def otvet(message : types.Message):
    await message.reply('Неизвестная команда')
    await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(otvet, content_types='text')