from os import curdir
import sqlite3 as sq
from handlers import commands_handler
from create_bot import dp
from aiogram import types

def sql_start():
    global base, cur
    base = sq.connect('spells.db')
    cur = base.cursor()
    if base:
        print('Data base connected')


async def sql_select_spell(message, search_text):
    if len(search_text) > 0:
        request = "SELECT * FROM spellindexbytechnique WHERE NAME LIKE \'%%%s%%\'"%(search_text)
        print(request)
        result=[]
        for r in cur.execute(request).fetchall():
            r_str=''
            for i in r:
                if len(str(i)) >0: r_str += ' ' + str(i)
            await message.reply(r_str) 


async def sql_select_base(message, search_base):
    level = '0'
    tech = ''
    form = ''
    for i in search_base.split():
        if i.capitalize() in ['Cr', 'In', 'Mu', 'Pe', 'Re']:
            tech = i.capitalize()
        elif i.capitalize() in ['An', 'Aq', 'Au', 'Co', 'He', 'Ig', 'Im', 'Me', 'Te', 'Vi']:
            form = i.capitalize()
        elif i.isdigit():
            level = i
    if tech !='' and form !='':
        request = "SELECT Base FROM TechForm WHERE Tech = \'%s\' and Form = \'%s\' and level = %s"%(tech, form, level)
        print(request)
        for r in cur.execute(request).fetchall():
            r_str=''
            for i in r:
                if len(str(i)) >0: r_str += ' ' + str(i)
            await message.reply(r_str) 


