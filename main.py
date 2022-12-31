from aiogram.utils import executor
from create_bot import dp
from handlers import client, other
#logging.basicConfig(level=logging.INFO)
# admin.register_handlers_admin(dp)
# other.register_handlers_other(dp)

client.register_handlers_clients(dp)
other.register_handlers_other(dp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

