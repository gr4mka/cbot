
import settings
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

from datetime import date
logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    my_keyboard = ReplyKeyboardMarkup([['Menu'], ['About']])
    update.message.reply_text(
        f"Здравствуй, пользователь!",
        reply_markup=my_keyboard)
#    cr_keyboard = ReplyKeyboardMarkup([['крипта', 'валюта', 'акции'],['новости'],['домой']])
#   update.message.reply_text(f'Что Вас интересует?', reply_markup=cr_keyboard)

def menu(update, context):
    cr_keyboard = ReplyKeyboardMarkup([['Button A', 'Button B', 'Button C'],['Button Z'],['home']])
    update.message.reply_text(f'Что Вас интересует?', reply_markup=cr_keyboard)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

#def what_day():
 #   my_keyboard = ReplyKeyboardMarkup()
 #   date = (f'Точная дата: {date.today}')
 #   update.message.reply_text(date, reply_markup=my_keyboard)

def main():
    bot = Updater(settings.API_KEY, use_context=True)

    dp = bot.dispatcher
    dp.add_handler
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('Menu', menu))
    dp.add_handler(MessageHandler(Filters.regex('^(Menu)$'), menu))
    dp.add_handler(MessageHandler(Filters.regex('^(home)$'), greet_user))
    dp.add_handler(CommandHandler('home', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
