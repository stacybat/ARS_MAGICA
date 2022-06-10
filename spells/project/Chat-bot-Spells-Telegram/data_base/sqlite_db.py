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
    search_text = "%" + search_text + "%"
    if len(search_text) > 2:
        request = "SELECT * FROM spellindexbytechnique WHERE NAME LIKE '%s'"%(search_text)
        print(request)
        flag = 1
        for r in cur.execute("SELECT * FROM spellindexbytechnique WHERE NAME LIKE  ? ", (search_text,)).fetchall():
            r_str=''
            for i in r:
                if len(str(i)) >0: r_str += ' ' + str(i)
            if r_str != '':
                await message.reply(r_str)
                flag = 0
        if flag:
            await message.reply('Nothing found for your request')
    else:
        await message.reply('You did not enter a search term')


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
        flag = 1
        for r in cur.execute("SELECT Base FROM TechForm WHERE Tech = ? and Form = ? and level = ?", (tech, form, level)).fetchall():
            r_str=''
            for i in r:
                if len(str(i)) >0: r_str += ' ' + str(i)
            if r_str != '':
                await message.reply(r_str)
                flag = 0
        if flag:
            await message.reply('Nothing found for your request')
    else:
        request = "SELECT Contumeliam FROM Contumeliam_csv  ORDER BY RANDOM() LIMIT 1"
        for r in cur.execute(request).fetchall():
            r_str=''
            for i in r:
                r_str += ' ' + str(i)
            await message.reply(r_str)
        

