
import settings
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, conversationhandler
from telegram import ReplyKeyboardMarkup, KeyboardButton

from datetime import date
from registration import registration_start
logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    my_keyboard = ReplyKeyboardMarkup([['Registration'], ['Menu'], ['About']])
#    context.user_data['name'] = registration(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f'Здравствуй, {username}!', reply_markup=my_keyboard)
""""
def registration(update, user_data): #пытаюсь прикрутить регистрацию пользователя
    if 'name' not in user_data:
        print('Как к Вам обращаться?')
        name = update.message.text
        return name(use_aliases=True)
    return user_data['name']
"""

def menu(update, context):
    menu_keyboard = ReplyKeyboardMarkup([['Input', 'Button B', 'Button C'],['Button Z'],['home']])
    update.message.reply_text(f'Что Вас интересует?', reply_markup=menu_keyboard)

def input(update, context): 
    my_keyboard = ReplyKeyboardMarkup([
    ['ID1', 'ID2', 'ID3', 'ID4', 'ID5'],
    ['ID6', 'ID7', 'ID8', 'ID9', 'ID10'],
    ['manual_mode'],
    ['home']])
    update.message.reply_text(f'Выберите ID валюты', reply_markup=my_keyboard)

#def writerCSV(message):
#    with open('Users.csv', 'w') as fileCVS:
#        fileCVS.write(message.text)

def about(update, context):
    about_text =  'Бот разработан в рамках обучающего курса Learn Python, 2022'
    my_keyboard = ReplyKeyboardMarkup([['Menu'],['home']])
    update.message.reply_text(f'{about_text}', reply_markup=my_keyboard)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

#def what_day():
#    my_keyboard = ReplyKeyboardMarkup()
#    date = (f'Точная дата: {date.today}')
#    update.message.reply_text(date, reply_markup=my_keyboard)

def main():
    bot = Updater(settings.API_KEY, use_context=True)

    dp = bot.dispatcher

    base = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Registration)$'), registration_start)
        ],
        states={},
        fallbacks=[])

    dp.add_handler(base)
    dp.add_handler
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('Menu', menu))
    dp.add_handler(CommandHandler('About', about))
    dp.add_handler(CommandHandler('home', greet_user))
    dp.add_handler(CommandHandler('Input', input))
    #dp.add_handler(CommandHandler('Registration', registration))
    dp.add_handler(MessageHandler(Filters.regex('^(Menu)$'), menu))
    #dp.add_handler(MessageHandler(Filters.regex('^(Registration)$'), registration))
    dp.add_handler(MessageHandler(Filters.regex('^(About)$'), about))
    dp.add_handler(MessageHandler(Filters.regex('^(home)$'), greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Input)$'), input))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
