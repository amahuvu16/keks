from aiogram import Bot
import os
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage    #хранение данных в оперативке

conf = {
	'name': 'BlgPadreShop_bot',
	'token': '5678271523:AAHS_Z-ggU-VmnYY-4oHV0Uyo_LcXUW182w',
	'tokenqiwi': '50df389829766f4f092156ff5904ea54',
	'phoneqiwi': '+79867571837'
}
storage = MemoryStorage()
bot = Bot(conf['token'])
# bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)