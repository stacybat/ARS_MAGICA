from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print('Bot is online')
    sqlite_db.sql_start()

from handlers import commands_handler

commands_handler.register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
