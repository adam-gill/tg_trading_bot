import os
import telebot
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
print(API_KEY)
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey whats up?")

bot.polling()