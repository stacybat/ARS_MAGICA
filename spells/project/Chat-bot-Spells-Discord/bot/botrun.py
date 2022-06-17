import discord
from discord.ext import commands
import os, sqlite3

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('ArsMagicaSpells is active')
    global base, cur
    base = sqlite3.connect('spells.db')
    cur = base.cursor()
    if base:
        print('Data base connected')

@bot.command()
async def h(ctx):
    await ctx.reply('''***Find a spell***
If you want to find a spell by the keywords, enter /fs *search_word*
    e.g.: /fs pilum
If you want to find a spell by the keywords with technique and/or form then type /fs *search_word* t:*Tech.* f:*Form*
    e.g.: /fs spell t:Re
    e.g.: /fs spell f:vi
    e.g.: /fs spell f:Vi t:re
    e.g.: /fs spell t:re f:VI
If you want to display a description of the spell add +d
    e.g.: /fs spell t:Re +d
    e.g.: /fs spell +d f:vi
    e.g.: /fs spell f:Vi +d t:re
    e.g.: /fs pilum +d

***Find a base***
If you want to find a base, enter /fb *Tech.* *Form* *Level*
    e.g.: /fb Cr Me 40
If you want to find a general base, you can enter level 0 or do not enter the level
    e.g.: /fb an re 0
    e.g.: /fb Mu Au''')




'''@bot.command()
async def h(ctx, *, arg):
    #author = ctx.ctx.author
    await ctx.reply(arg)'''

@bot.command()
async def fs(ctx, *, arg):
    search_text = ''
    search_text = " ".join(arg.split())
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
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? ", (search_words,)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await ctx.reply('Nothing found for your request')
            else:
                await ctx.reply(result)
        elif len(search_words) > 1 and tech != '' and form == '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND tech = '%s'"%(search_words, tech)
            print(request)
            flag = 1
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ?", (search_words, tech)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await ctx.reply('Nothing found for your request')
            else:
                await ctx.reply(result)
        elif len(search_words) > 1 and tech == '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND form = '%s'"%(search_words, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND form = ?", (search_words, form)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await ctx.reply('Nothing found for your request')
            else:
                await ctx.reply(result)
        elif len(search_words) > 1 and tech != '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE '%s'AND tech = '%s' AND form = '%s'"%(search_words, tech, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ? AND form = ?", (search_words, tech, form)).fetchall():
                r_str = ''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)                
                if r_str != '':
                    flag = 0
                    result += r_str + '\n\n'
                
            if flag:
                await ctx.reply('Nothing found for your request')
            else:
                await ctx.reply(result)

        else:
            await ctx.reply('You did not enter a search term')
    else:
        if len(search_words) > 1 and tech == '' and form == '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s'"%(search_words)
            print(request)
            flag = 1
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? ", (search_words,)).fetchall():
                r_str=''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)
                if r_str != '':
                    await ctx.reply(r_str)
                    flag = 0
            if flag:
                await ctx.reply('Nothing found for your request')
                
        elif len(search_words) > 1 and tech != '' and form == '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND tech = '%s'"%(search_words, tech)
            print(request)
            flag = 1
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ?", (search_words, tech)).fetchall():
                r_str=''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)
                if r_str != '':
                    await ctx.reply(r_str)
                    flag = 0
            if flag:
                await ctx.reply('Nothing found for your request')
        elif len(search_words) > 1 and tech == '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s' AND form = '%s'"%(search_words, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND form = ?", (search_words, form)).fetchall():
                r_str=''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)
                if r_str != '':
                    await ctx.reply(r_str)
                    flag = 0
            if flag:
                await ctx.reply('Nothing found for your request')
        elif len(search_words) > 1 and tech != '' and form != '':
            request = "SELECT name_of_the_spell, '\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE '%s'AND tech = '%s' AND form = '%s'"%(search_words, tech, form)
            print(request)
            flag = 1
            for r in cur.execute("SELECT '***', name_of_the_spell, '***\n', tech, form, req, level, spell_range, duration, target, spell_type, base_of_spell, spell_mod, '\n', source, '\n', description \
                FROM Spells WHERE name_of_the_spell LIKE  ? AND tech = ? AND form = ?", (search_words, tech, form)).fetchall():
                r_str=''
                for i in r:
                    if len(str(i)) >0: r_str += ' ' + str(i)
                if r_str != '':
                    await ctx.reply(r_str)
                    flag = 0
            if flag:
                await ctx.reply('Nothing found for your request')

        else:
            await ctx.reply('You did not enter a search term')

            

@bot.command()
async def fb(ctx, *, arg):
    search_base = ''
    search_base = " ".join(arg.split())
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
                await ctx.reply(r_str)
                flag = 0
        if flag:
            await ctx.reply('Nothing found for your request')
    else:
        request = "SELECT Contumeliam FROM Contumeliam_csv  ORDER BY RANDOM() LIMIT 1"
        for r in cur.execute(request).fetchall():
            r_str=''
            for i in r:
                r_str += ' ' + str(i)
            await ctx.reply(r_str)


bot.run(os.getenv('TOKEN'))
