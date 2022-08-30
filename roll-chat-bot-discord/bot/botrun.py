# Импортируем библиотеки
import random


def help():
    text = '''\nСписок команд:
            /r - simple
            /s - stress
            +/-N - modifier value
            /N - number of botchs
            N - number of rolls
            where N - is a number
            Commands are separated by spaces'''
    return text

# Функция симпл броска
def simple_dice(num, mod):
    rolls = []
    
    for i in range(num):
        roll = random.randrange(1,11)
        rolls.append('Result (mod = ' + str(mod) + '): ' + str(roll + mod) + '  Roll: ' + str(roll))
    
    return rolls

# Функция переброса 1 при стрессовом броске
def stress_1(rolls_stress_1):
    roll = random.randrange(0,10)
    rolls_stress_1.append(roll)
    result = 1
    mul = 1
    #print(rolls_stress_1, mul)
    if roll == 1:
        stress_1(rolls_stress_1)

    mul = pow(2,(len(rolls_stress_1)-1))
    #print(mul)
    if rolls_stress_1[-1] == 0:
        r = 10
    else:
        r = rolls_stress_1[-1]
    result = r*mul
    
    return result, rolls_stress_1

# Функция ботч броска
def botch_dice(botch_num):
    botch_result = 0
    botch_rolls = []
    for _ in range(botch_num):
        roll = random.randrange(0,10)
        botch_rolls.append(roll)
        if roll == 0:
            botch_result +=1
    
    return botch_result, botch_rolls

# Функция стрессового броска
def stress_dice(num, mod, botch):
    # Объявляем переменную stress_results, которая содержит все результаты стрессового броска
    stress_results = [["" for j in range(3)] for i in range(num)]
    all_results = []  

    # Делаем в цикле стрессовые броски, num - количество брошенных кубов
    for i in range(num):
        rolls = []
        botch_result = 0
        roll = random.randrange(0,10)

        # Определяем есть ли ботчи и взрывы
        if roll == 0:
            botch_result, botch_rolls = botch_dice(botch)
            rolls.append(roll)
        elif roll == 1:
            rolls.append(roll)
            result_stress, rolls = stress_1(rolls)
        else:
            rolls.append(roll)

        # Оформляем результат и добавляем если надо модификатор
        if roll == 0 and botch_result == 0:
            result = roll + mod
            stress_results[i][2] = 'No Botch'
        elif roll == 0 and botch_result == 1:
            result = 0
            stress_results[i][2] = '1 Botch' + ' Botch roll: ' + str(botch_rolls)
        elif roll == 0 and botch_result > 1:
            result = 0
            stress_results[i][2] = str(botch_result) + ' Botchs' + ' Botch rolls: ' + str(botch_rolls)
        elif roll == 1:
            result = result_stress + mod
            stress_results[i][2] = ''
        else:
            result = roll + mod
            stress_results[i][2] = ''
        stress_results[i][0] = 'Result (mod = ' + str(mod) + '): ' + str(result)
        stress_results[i][1] = 'Rolls: ' + str(rolls)
        all_results.append(stress_results[i][0] + '  ' + stress_results[i][1] + '  ' + stress_results[i][2])       
    
    return all_results

# Функция в которой отрабатывается стрессовый бросок

def command_s(request):
    request=request.lower()
    print(request)

    # разобьем команду пробелами на части
    command = request.split()
    dice_num = 1
    dice_botch = 1
    modificator = 0
    # Присвоим переменным значение из введенной команды
    for n in command:
        #comm.append(n)
        #print(type(n))
        if  n.isdigit():
            dice_num = int(n)
        elif n[0] == '/' and str(n[1:]).isdigit():
            dice_botch = int(n[1:])
        elif (n[0] == '+' or n[0] == '-') and str(n[1:]).isdigit():
            modificator = modificator + int(n)
        else:
            continue
    # Запускаем функцию либо симпл броска либо стресс броска     
    result = stress_dice(dice_num, modificator, dice_botch)
    
    return result

# Функция в которой отрабатывается симпл бросок

def command_r (request):
    request=request.lower()
    print(request)

    # разобьем команду пробелами на части
    command = request.split()
    # Количество бросаемых кубов 1, модификатор 0
    dice_num = 1
    modificator = 0
    # Присвоим переменным значение из введенной команды
    for n in command:
        #comm.append(n)
        #print(type(n))
        if  n.isdigit():
            dice_num = int(n)
        elif (n[0] == '+' or n[0] == '-') and str(n[1:]).isdigit():
            modificator = modificator + int(n)
        else:
            continue
    # Запускаем функцию симпл броска  
    result = simple_dice(dice_num, modificator)
       
    return result


import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')

@bot.command()
async def test(ctx):
    await ctx.reply('Hi')
    print('Куб на старте')

@bot.command()
async def s(ctx, *,arg):
    bot_answer = command_s(arg)
    for s in bot_answer:     
        print(s)
        #Отправляем результаты бросков построчно
        await ctx.reply(s)

@bot.command()
async def r(ctx, *,arg):
    bot_answer = command_r(arg)
    for r in bot_answer:     
        print(r)
        #Отправляем результаты бросков построчно
        await ctx.reply(r)


bot.run(os.getenv('TOKEN'))


