import config
import telebot

#123
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def wellcome(message):
    bot.send_message(message.chat.id, 'Здарова прогеры, я крутой бот ! \nМеня создал гений')


@bot.message_handler(content_types=['Здарова'])
def hello(message):
    bot.send_message(message.chat.id, f'Здарова {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def test(message):
    if 'тест222' in message.text.lower():
        bot.send_message(message.chat.id, 'Тест')
<<<<<<< HEAD
=======

bot.polling()

>>>>>>> ab0332ae5691fc896c8abc73c089ac067bbec510
