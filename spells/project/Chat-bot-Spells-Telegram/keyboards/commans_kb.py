from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/search')
b2 = KeyboardButton('/help')
kb_commands = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_commands.add(b1).add(b2)