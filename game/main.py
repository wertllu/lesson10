import telebot
from telebot import types
from game import game_help, game_get_random, game_get_result
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
	# game_res = game_play(message.text)
	# bot.send_message(message.chat.id, text=game_res)
	print(f'{message.from_user.username}: {message.text}')
	user_option = message.text
	bot.send_message(message.chat.id, text=f'Ви обрали {user_option}')
	ai_option = game_get_random()
	bot.send_message(message.chat.id, text=f'Я обрала {ai_option}')
	bot.send_message(message.chat.id, text=game_get_result(user_option, ai_option))

bot.infinity_polling() 