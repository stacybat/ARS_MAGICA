#from os import curdir
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
    search_words = ''
    tech = ''
    form = ''
    desc_flag = 0
    result = ''
    print(search_text)
    for w in search_text.split():
        if w[0:2] == 'f:' and w[2:].capitalize() in ['An', 'Aq', 'Au', 'Co', 'He', 'Ig', 'Im', 'Me', 'Te', 'Vi']:
            form = w[2:].capitalize()
        elif w[0:2] == 't:' and w[2:].capitalize() in ['Cr', 'In', 'Mu', 'Pe', 'Re']:
            tech = w[2:].capitalize()
        elif w[0:2] == '+d':
            desc_flag = 1
        else:
            search_words += "%" + w        
    search_words = search_words + "%"
    if desc_flag == 0:
        if len(search_words) > 1 and tech == '' and form == '':
            request = "SELECT name_of_the_spell, '\n',  tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE '%s'"%(search_words)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? ", (search_words,)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await message.reply('Nothing found for your request')
            else:
                await message.reply(result)
        elif len(search_words) > 1 and tech != '' and form == '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND tech = '%s'"%(search_words, tech)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ?", (search_words, tech)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await message.reply('Nothing found for your request')
            else:
                await message.reply(result)
        elif len(search_words) > 1 and tech == '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND form = '%s'"%(search_words, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND form = ?", (search_words, form)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await message.reply('Nothing found for your request')
            else:
                await message.reply(result)
        elif len(search_words) > 1 and tech != '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE '%s'AND tech = '%s' AND form = '%s'"%(search_words, tech, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ? AND form = ?", (search_words, tech, form)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await message.reply('Nothing found for your request')
            else:
                await message.reply(result)

        else:
            await message.reply('You did not enter a search term')
    else:
        if len(search_words) > 1 and tech == '' and form == '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s'"%(search_words)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? ", (search_words,)).fetchall():
                r_str=''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)
                if r_str != '':
                    await message.reply(r_str)
                    flag = 0
            if flag:
                await message.reply('Nothing found for your request')
                
        elif len(search_words) > 1 and tech != '' and form == '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND tech = '%s'"%(search_words, tech)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ?", (search_words, tech)).fetchall():
                r_str=''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)
                if r_str != '':
                    await message.reply(r_str)
                    flag = 0
            if flag:
                await message.reply('Nothing found for your request')
        elif len(search_words) > 1 and tech == '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND form = '%s'"%(search_words, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND form = ?", (search_words, form)).fetchall():
                r_str=''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)
                if r_str != '':
                    await message.reply(r_str)
                    flag = 0
            if flag:
                await message.reply('Nothing found for your request')
        elif len(search_words) > 1 and tech != '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s'AND tech = '%s' AND form = '%s'"%(search_words, tech, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ? AND form = ?", (search_words, tech, form)).fetchall():
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
        request = "SELECT Base FROM BaseTechForm WHERE Tech = \'%s\' and Form = \'%s\' and level = %s"%(tech, form, level)
        print(request)
        flag = 1
        for r in cur.execute("SELECT Base FROM BaseTechForm WHERE Tech = ? and Form = ? and level = ?", (tech, form, level)).fetchall():
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
        

