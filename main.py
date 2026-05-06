from telebot import TeleBot

TOKEN = '8756105455:AAEnv9djVpAghAd6U0KyQq3buZJLGlRRCzQ'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую тебя в моем боте! Я могу помочь тебе с различными задачами. Просто напиши мне, и я постараюсь помочь тебе!')     


bot.polling()