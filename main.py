import telebot
import config
import BIT
import USD
import EUR
import SBER

from telebot import types


bot = telebot.TeleBot(config.token)


# Start commands
@bot.message_handler(commands=['start'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Валюта', callback_data='Currency')
    btn2 = types.InlineKeyboardButton('Ценные бумаги', callback_data='Securities')
    btn3 = types.InlineKeyboardButton('Крипта', callback_data='Crypt')
    btn4 = types.InlineKeyboardButton('Отзыв', callback_data='Feedback')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}!</b>!\nЧто Вас интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


# USD command
@bot.message_handler(commands=['Валюта'])
def USD(message):
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Доллар к рублю  = {USD.USD()} руб."
    bot.send_message(message.chat.id, send_mess)


# EUR commands
@bot.message_handler(commands=['EUR'])
def EUR(message):
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Евро к рублю  = {EUR.EUR()} руб."
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(commands=['SBER'])
def SBER(message):
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 акция Сбербанка к рублю  = {SBER.SBER()} руб."
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(commands=['BIT'])
def BIT(message):
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Биткоин к рублю  = {BIT.bit()} руб."
    bot.send_message(message.chat.id, send_mess)


bot.polling(none_stop=True)
