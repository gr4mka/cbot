from telegram import ReplyKeyboardRemove

def registration_start(update, context):
    update.message.reply_text(
        'Введите информацию_1:',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'info1'