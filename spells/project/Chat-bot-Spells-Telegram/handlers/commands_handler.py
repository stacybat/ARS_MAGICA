from aiogram import types, Dispatcher
from create_bot import dp
from keyboards import kb_commands


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply('Привет! Что ищем?', reply_markup=kb_commands)


#@dp.message_handler()
async def search_command(message : types.Message):
    await message.answer(message.text)
    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(search_command)
