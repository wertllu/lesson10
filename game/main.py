import telebot
from telebot import types
from game import game_help,game_play
bot = telebot.TeleBot("5799033377:AAESuDz_aZQ68oF7eKHPSEUhP5IkRFxb2JM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("камінь")
	btn2 = types.KeyboardButton("ножиці")
	btn3 = types.KeyboardButton("папір")
	markup.add(btn1, btn2, btn3)
	bot.send_message(message.chat.id, text=game_help(), reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	game_res = game_play(message.text)
	bot.send_message(message.chat.id, text=game_res)

bot.infinity_polling() 