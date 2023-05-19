# starting with venv
# install commands
# python.exe -m pip install --upgrade pip
# pip install requests
# pip install beautifulsoup4
# pip install PyTelegramBotAPI

import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good/'
API_KEY = '6149140088:AAGBa280FabMnFvjvasNb7p1jpXOW80t_q0'
def parser(url):
    r = requests.get(url)

# print(r.status_code)
# print(r.text)

    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

# print(anekdots)

    # clearAnekdots = [c.text for c in anekdots]
    # print(clearAnekdots)

listOfJokes = parser(URL)
random.shuffle(listOfJokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['Start'])

def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте чтобы посмеяться введите любую цифру')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, listOfJokes[0])
        del listOfJokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру')
bot.polling()