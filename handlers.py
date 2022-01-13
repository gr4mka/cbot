from glob import glob
from telegram import ReplyKeyboardMarkup, KeyboardButton

from db import db, get_or_create_user, subscriber, unsubscriber

def greet_user(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    text = 'Вызван /start'
    print(text)
    my_keyboard = ReplyKeyboardMarkup([['Registration'], ['Menu'], ['About']])
    username = update.effective_user.first_name  # изначально обращамся к пользователю так, как он сам себя называет в телеге
 #   text = update.message.text
    update.message.reply_text(f'Здравствуйте, {username}!', reply_markup=my_keyboard)

def subscribe(update, context):
    user = get_or_create_user(db, update.effective_user, update.message)
    subscriber(db, user)
    update.message.reply_text('Вы подписались. Правильный выбор!')

def unsubscribe(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    unsubscriber(db, user)
    update.message.reply_text('Вы отписались. А зря :(')

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

def about(update, context):
    about_text =  'Бот разработан в рамках обучающего курса Learn Python, 23й набор (2022)'
    my_keyboard = ReplyKeyboardMarkup([['Menu'],['home']])
    update.message.reply_text(f'{about_text}', reply_markup=my_keyboard)

def talk_to_me(update, context):
    user_text = update.message.text
    print(f'Ваша команда', {user_text}, 'не распознана')
    update.message.reply_text(user_text)
    