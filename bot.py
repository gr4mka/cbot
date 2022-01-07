
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, conversationhandler
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings

# from datetime import date

from registration import registration_start, registration_name, registration_comment, registration_skip
from handlers import greet_user, talk_to_me, menu, input, about

def main():
    bot = Updater(settings.API_KEY, use_context=True)

    dp = bot.dispatcher

    base = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Registration)$'), registration_start)
        ],
        states={
            'name':[MessageHandler(Filters.text, registration_name)],
            'rating': [MessageHandler(Filters.regex('^(1|2|3|4|5)$'), registration_rating)],
            'comment':[
                CommandHandler('skip', registration_skip),
                MessageHandler(Filters.text, registration_comment)
                ]
            },
        fallbacks=[]
    )

    dp.add_handler(base)
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('Menu', menu))
    dp.add_handler(CommandHandler('About', about))
    dp.add_handler(CommandHandler('home', greet_user))
    dp.add_handler(CommandHandler('Input', input))
    dp.add_handler(CommandHandler('Registration', registration_start))
    dp.add_handler(MessageHandler(Filters.regex('^(Menu)$'), menu))
    dp.add_handler(MessageHandler(Filters.regex('^(Registration)$'), registration_start))
    dp.add_handler(MessageHandler(Filters.regex('^(About)$'), about))
    dp.add_handler(MessageHandler(Filters.regex('^(home)$'), greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Input)$'), input))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
