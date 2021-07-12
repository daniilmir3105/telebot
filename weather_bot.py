import telebot
# import pyowm
import weather

weather_obj = weather.weather_information()

bot = telebot.TeleBot('1863707361:AAGFEtbRnQaRZwPQ5GNdsRhXy98USeGBIvY')

@bot.message_handler(commands=['start', 'help'])
def send_sticker(message):
    # sendSticker
    chat_id = message.chat.id
    sti = open(r'C:\Users\Daniil\Downloads\sticker_hello.webp', 'rb')
    bot.send_sticker(chat_id, sti)

@bot.message_handler(func=lambda message: True)
def answer(message):
	bot.reply_to(message, weather_obj.get_info(message.text))

bot.polling(none_stop = True)