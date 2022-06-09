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

async def sql_select_command(message, search_text):
    if len(search_text) > 0:
        request = "SELECT * FROM spellindexbytechnique WHERE NAME LIKE \'%%%s%%\'"%(search_text)
        print(request)
        result=[]
        for r in cur.execute(request).fetchall():
            r_str=''
            for i in r:
                if len(str(i)) >0: r_str += ' ' + str(i)
            await message.reply(r_str) 
            
            #result.append(r_str)
    #print(*result, sep = '\n')
    #return result