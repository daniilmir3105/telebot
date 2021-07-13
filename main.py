import telebot 

bot = telebot.TeleBot("TOKEN")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Скажи, пожалуйста, какие функции у тебя есть?', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Приветствую, чем я могу вам помочь?')
    
# become messages from user and return echo-message back
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	# bot.reply_to(message, message.text)
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'Скажи, пожалуйста, какие функции у тебя есть?':
        bot.send_message(message.chat.id, 'Я пока ничего не умею(((', reply_markup=keyboard1)
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, добрый человек!', reply_markup=keyboard1)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Давай познакомимся?':
        bot.send_message(message.from_user.id, "Дава, как тебя зовут?")
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surnme)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message('Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

bot.polling(none_stop=True)