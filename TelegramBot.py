# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import telebot
import requests
import random





bot = telebot.TeleBot('846482624:AAERvZ94oVMrqLULMsqQI-ro0Ce-H-b3by0')
page = 'https://www.anekdot.ru/random/anekdot/'
headers = {'User-Agent': 'My User Agent 1.0'}


def new_anekdot():
    response = requests.get(page, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    anekdots = soup.find_all("div", class_="text", limit=4)
    clear_raw = random.choice(anekdots).get_text()
    return clear_raw


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if repr(message.text) == "привет":
        bot.send_message(message.from_user.id, "привет в ответ")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'привет'")
    elif message.text == "/anekdot":
        bot.send_message(message.from_user.id, new_anekdot())
    elif message.text == 'пока':
        bot.send_message(message.from_user.id, "пока и тебе")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)