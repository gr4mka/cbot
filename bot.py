
import settings
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, messagehandler
from telegram import ReplyKeyboardMarkup, replymarkup

from datetime import date


def greet_user(update, context):
    print('Вызван /start')
    my_keyboard = ReplyKeyboardMarkup([['Который час?']])
    update.message.reply_text(
        f'Здравствуйте! Что Вас интересует?',
        reply_markup=my_keyboard
    )

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def what_day():
#    my_keyboard = ReplyKeyboardMarkup()
    print(f'Точная дата: {date.today}')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("date", what_day))
    dp.add.handler(messagehandler(Filters.regex('^(Который час?)$'), what_day))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
