import telebot

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello, Daniel, how are you?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop=True)
