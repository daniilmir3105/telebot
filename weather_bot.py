import telebot
import pyowm
import weather

weather_obj = weather.weather_information()

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start', 'help'])
def send_sticker(message):
    # sendSticker
    chat_id = message.chat.id
    sti = open(r'C:\Users\Daniil\Downloads\sticker_hello.webp', 'rb')
    bot.send_sticker(chat_id, sti)
    bot.send_message(message.chat.id, 'В каком городе вы хотите узнать погоду?')

@bot.message_handler(func=lambda message: True)
def answer(message):
    try:
        bot.reply_to(message, weather_obj.get_info(message.text))
    except pyowm.commons.exceptions.NotFoundError:
        bot.reply_to(message, 'Простите, я не совсем вас понял...')


bot.polling(none_stop = True)