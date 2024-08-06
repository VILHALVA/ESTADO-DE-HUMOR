from TOKEN import TOKEN
import telebot
import random
import json

bot = telebot.TeleBot(TOKEN)

with open('HUMOR.json', 'r', encoding='utf-8') as f:
    humores = json.load(f)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Envie o comando /eu para descobrir seu estado de humor hoje.")

@bot.message_handler(commands=['eu'])
def send_mood(message):
    nome = message.from_user.first_name
    percentual = random.randint(1, 100)
    humor = random.choice(humores)
    resposta = f"{nome}, você está {percentual}% {humor} hoje."
    bot.reply_to(message, resposta)

bot.polling()
