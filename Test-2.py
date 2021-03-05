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
    btn2 = types.InlineKeyboardButton('Ценные бумаги', callback_data='Shares')
    btn3 = types.InlineKeyboardButton('Крипта', callback_data='Crypt')
    btn4 = types.InlineKeyboardButton('Отзыв', callback_data='Feedback')
    markup.add(btn1, btn2, btn3, btn4)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}!</b>!\nЧто Вас интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def menu1(call):
    if call.data == 'Currency':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Доллар', callback_data='USD')
        btn2 = types.InlineKeyboardButton('Евро', callback_data='EUR')
        btn3 = types.InlineKeyboardButton('Назад', callback_data='BACK')
        markup.add(btn1, btn2, btn3)
        send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какая Вас интересует валюта?", parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(send, menu2)
    elif call.data == 'Shares':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Сбербанка', callback_data='SBER')
        btn2 = types.InlineKeyboardButton('Tesla', callback_data='TESLA')
        btn3 = types.InlineKeyboardButton('Назад', callback_data='BACK')
        markup.add(btn1, btn2, btn3)
        send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какие Вас интересует Ценные бумаги?", parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(send, menu2)
    elif call.data == 'Crypt':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('К Рублю', callback_data='TO_THE_RUB')
        btn2 = types.InlineKeyboardButton('К Доллару', callback_data='TO_THE_USD')
        btn3 = types.InlineKeyboardButton('Назад', callback_data='BACK')
        markup.add(btn1, btn2,btn3)
        send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какие Вас интересует криптовалюта?", parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(send, menu2)
    elif call.data == 'Feedback':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Оставьте свой отзыв или предложение', callback_data='Feedback')
        btn2 = types.InlineKeyboardButton('Назад', callback_data='BACK')
        markup.add(btn1, btn2)
        send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Оставьте свой отзыв или предложение", reply_markup=markup)
        bot.register_next_step_handler(send, menu2)


@bot.callback_query_handler(func=lambda call: True)
def menu2(call):
    if call.data == 'USD':
        send_mess = f"{call.from_user.first_name} {call.from_user.last_name}\nНа данный момент 1 Доллар к рублю  = {USD.USD()} руб."
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=send_mess)
    elif call.data == 'TO_THE_RUB':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('BITrub', callback_data='BIT_RUB')
        btn2 = types.InlineKeyboardButton('ETHrub', callback_data='ETH_RUB')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Какие Вас интересует криптовалюта?", parse_mode='html', reply_markup=markup)



# USD command
@bot.message_handler(commands=['USD'])
def USD(message):
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Доллар к рублю  = {USD.USD()} руб."
    bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id, text=send_mess)


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
    send_mess = f"{message.from_user.first_name} {message.from_user.last_name}\nНа данный момент 1 Биткоин к рублю  = {BIT.bit_rub()} руб."
    bot.send_message(message.chat.id, send_mess)


bot.polling(none_stop=True)
