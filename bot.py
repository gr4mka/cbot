
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, conversationhandler

import settings
logging.basicConfig(filename="bot.log", level=logging.INFO)

from handlers import greet_user, talk_to_me, menu, input, about, subscribe, unsubscribe
from registration import registration_start, registration_name, registration_choice, registration_comment, registration_skip, registration_mistake
from jobs import send_hello

def main():
    bot = Updater(settings.API_KEY, use_context=True)

    jq = bot.job_queue
    jq.run_repeating(send_hello, interval=60)

    dp = bot.dispatcher

    registration = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Registration)$'), registration_start)
        ],
        states={
            'name':[MessageHandler(Filters.text, registration_name)],
            'choice': [MessageHandler(Filters.regex('^(тык1|тык2|тык3|тык4|тык5)$'), registration_choice)],
            'comment':[
                CommandHandler('skip', registration_skip),
                MessageHandler(Filters.text, registration_comment)
                ]
            },
        fallbacks=[MessageHandler(Filters.text, registration_mistake)
        ]
    )

    dp.add_handler(registration)
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('Menu', menu))
    dp.add_handler(CommandHandler('About', about))
    dp.add_handler(CommandHandler('home', greet_user))
    dp.add_handler(CommandHandler('Input', input))
    dp.add_handler(CommandHandler('Registration', registration_start))
    dp.add_handler(CommandHandler('subscribe', subscribe))
    dp.add_handler(CommandHandler('unsubscribe', unsubscribe))
    dp.add_handler(MessageHandler(Filters.regex('^(Menu)$'), menu))
    dp.add_handler(MessageHandler(Filters.regex('^(subscribe)$'), subscribe))
    dp.add_handler(MessageHandler(Filters.regex('^(unsubscribe)$'), unsubscribe))
    dp.add_handler(MessageHandler(Filters.regex('^(Registration)$'), registration_start))
    dp.add_handler(MessageHandler(Filters.regex('^(About)$'), about))
    dp.add_handler(MessageHandler(Filters.regex('^(home)$'), greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Input)$'), input))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    

    bot.start_polling()
    bot.idle()


if __name__ == "__main__":
    main()
