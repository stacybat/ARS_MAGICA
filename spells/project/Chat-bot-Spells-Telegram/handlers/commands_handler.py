from aiogram import types, Dispatcher
from create_bot import dp
from data_base import sqlite_db
#from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

#class FSMqueery_search(StatesGroup):
#    q_search = State()
#    result = State()


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    #await FSMqueery_search.q_result.set()
    await message.reply('Hello! If you want to search for a spell by a keyword, enter /f *search_word*')
    print('1')
    #await FSMqueery_search.q_search.set()
    print('2')
    


#@dp.message_handler()
#async def search_command(message : types.Message):
    #await FSMqueery_search.q_search.set()
    #await message.reply('Search text')

async def input_search_text(message: types.Message):
    #, state: FSMContext):
    #async with state.proxy() as data:
    #    data['q_search'] = message.text
    print(message.text)
    search_text = " ".join(message.text.split()[1:])
    #await FSMqueery_search.next()
    await sqlite_db.sql_select_command(message, search_text)
    #request=message.text.split()
    #print(request)
    #async with state.proxy() as data:
        #data['q_search'] = message.text.split()
        #print(data['q_search'])
    #await message.reply(sqlite_db.sql_select_command(data['q_search']))
    #await FSMqueery_search.next()
    #async with state.proxy() as data:
    #await FSMqueery_search.next()
    #await message.reply('str(data)')
    #await state.finish()
    #for r in
     #   await message.reply(sqlite_db.sql_select_command(" ".join(request[1:])))

    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    #dp.register_message_handler(search_command, commands=['find'])#, state=None)
    dp.register_message_handler(input_search_text, commands=['find'])
    #state=FSMqueery_search.q_search)