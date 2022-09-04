from game import game_help,game_play

# bot = telebot.TeleBot("5799033377:AAESuDz_aZQ68oF7eKHPSEUhP5IkRFxb2JM")

# @bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	bot.reply_to(message, game_help())

# @bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, game_play(message.text))
# 	# bot.(message, message.text)
# 	play_game(message)

# bot.infinity_polling() 


print(game_help())

print(game_play('1'))
print(game_play('2'))
print(game_play('3'))

