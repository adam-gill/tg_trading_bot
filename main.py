import os
import telebot
from dotenv import load_dotenv

load_dotenv()
# test 2

API_KEY = os.getenv('API_KEY')
print(API_KEY)
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey whats up?")

@bot.message_handler(commands=['gn'])
def gn(message):
    bot.reply_to(message, "Goodnight 🌙")

@bot.message_handler(commands=['gm'])
def gm(message):
    bot.reply_to(message, "Good morning ☀️")

bot.polling()