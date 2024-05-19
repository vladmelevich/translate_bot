import telebot
from deep_translator import GoogleTranslator
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('EN/RU',callback_data='анг')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('RU/EN',callback_data='ру')
    markup.row(btn2)
    bot.send_message(message.chat.id,'Привет.Это бот для перевода текста с русского языка на английский и нааборот!Выберите как надо переводить',reply_markup=markup)

@bot.callback_query_handler(func=lambda callback:True)
def cal_fun(callback):
    if callback.data == 'анг':
        bot.send_message(callback.message.chat.id,'введите слово на английском языке')
        bot.register_next_step_handler(callback.message,england)
    elif callback.data == 'ру':
        bot.send_message(callback.message.chat.id, 'введите слово на русском языке')
        bot.register_next_step_handler(callback.message, russia)

def england(message):
    en = message.text
    translate = GoogleTranslator(source='en',target='ru')
    trans = translate.translate(f'{en}')
    bot.send_message(message.chat.id,f'{trans}')

def russia(message):
    rus = message.text
    translate = GoogleTranslator(source='ru', target='en')
    trans = translate.translate(f'{rus}')
    bot.send_message(message.chat.id, f'{trans}')

bot.polling(none_stop=True)