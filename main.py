import telebot
import requests
import url
import config

from telebot import types
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.token)


# Start commands
@bot.message_handler(commands=['start'])
def menu(message):
    markup = types.ReplyKeyboardMarkup (row_width=5)
    btn1 = types.KeyboardButton ('/EUR')
    btn2 = types.KeyboardButton ('/USD')
    btn3 = types.KeyboardButton ('/SBER - Акции Сбербанка')
    btn4 = types.KeyboardButton ('/BIT - Биткоин')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}!</b>!\nЧто Вас интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)




# USD command
@bot.message_handler(commands=['USD'])
def USD(message):
    full_page = requests.get(url.urlUSDrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Доллар к рублю  = {convert[0].text}."
    bot.send_message(message.chat.id, send_mess)



# EUR commands
@bot.message_handler(commands=['EUR'])
def EUR(message):
    full_page = requests.get(url.urlEURrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Евро к рублю  = {convert[0].text}."
    bot.send_message(message.chat.id, send_mess)



@bot.message_handler(commands=['SBER'])
def start_message(message):
    full_page = requests.get(url.urlSBERrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "IsqQVc", "class": "NprOob", "class": "XcVN5d"})
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 акция Сбербанка к рублю  = {convert[0].text}."
    bot.send_message(message.chat.id, send_mess)


@bot.message_handler(commands=['BIT'])
def start_message(message):
    full_page = requests.get(url.urlBITrub, headers=url.headers)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Биткоин к рублю  = {convert[0].text}."
    bot.send_message(message.chat.id, send_mess)




@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'доллар':
            bot.send_message(message.chat.id, 'EUR')
            bot.register_next_step_handler(message, USD)
        elif message.text == 'евро':
            bot.send_message(message.chat.id, '/EUR')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


bot.polling(none_stop=True)
