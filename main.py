import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as b
url='https://www.banki.ru/products/currency/usd/'
API_KEY='APIKEY'
while True:
        def parser(url):
            r=requests.get(url)
            soup=b(r.text, 'html.parser') 
            kurs=soup.find_all('div', {'class': 'currency-table__large-text'}) #text-2xl bg-positive-light  text-2xl
            return [c.text for c in kurs]

        dollar_kurs=parser(url)
        bot = telebot.TeleBot(API_KEY)
        @bot.message_handler(commands=['start'])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            Kuarse=types.KeyboardButton('Курс доллара')
            start = types.KeyboardButton("/start")
            markup.add(Kuarse,start)
            bot.send_message(message.chat.id, "Привет, {0.first_name}! Я тестовый бот, показывающий курсы валют!".format(message.from_user), reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def course(message):
            if (message.text == "Курс доллара"):
                bot.send_message(message.chat.id,text="Сегодняшний курс доллара к рублю: 1$ = "+ dollar_kurs[0])
            elif (message.text == "/start"):
                return
        if __name__ == '__main__':
            parser(url)
        bot.polling(none_stop=True)


