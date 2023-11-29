import telebot

bot = telebot.TeleBot('6758899435:AAFfbyWb6ywfNQbk4RpjwYC8zP7-c6GIG1c')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '_привет!_ как дела?', parse_mode='Markdown')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'хорошая погода сегодня. \n*что скажешь?*', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'ЭТО [ССЫЛКА](https://pastebin.com/)', parse_mode='Markdown')


bot.infinity_polling()






