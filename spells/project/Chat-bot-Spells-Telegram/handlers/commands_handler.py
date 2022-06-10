from aiogram import types, Dispatcher
from create_bot import dp
from data_base import sqlite_db
from aiogram.dispatcher.filters.state import State, StatesGroup
import string


async def command_start(message: types.Message):  
    await message.reply('Hello! This bot is looking for pages where the spell is described in the books of Ars Magica and looking for spell bases')

    
async def command_help(message: types.Message):
    await message.reply('''***Find a spell***
If you want to find a spell, enter /fs *search_word*
    e.g.: /fs pilum\n
***Find a base***
If you want to find a base, enter /fb *Tech.* *Form* *Level*
    e.g.: /fb Cr Me 40
If you want to find a general base, you can enter level 0 or do not enter the level
    e.g.: /fb an re 0
    e.g.: /fb Mu Au''')

  
async def input_search_spell(message: types.Message):
    print(message.text)
    search_text = ''
    search_text = " ".join(message.text.split()[1:])
    await sqlite_db.sql_select_spell(message, search_text)


async def input_search_base(message: types.Message):
    print(message.text)
    search_base = " ".join(message.text.split()[1:])
    await sqlite_db.sql_select_base(message, search_base)


def register_handlers(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(input_search_spell, commands=['fs'])
    dp.register_message_handler(input_search_base, commands=['fb'])