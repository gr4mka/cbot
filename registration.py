from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def registration_start(update, context):
    update.message.reply_text(
        'Введите имя и фамилию:',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'
def registration_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text ('Введите имя и фамилию')
        return 'name'
    else:
        context.user_data['registration'] = {'name': user_name}
        reply_keyboard = [['1', '2', '3', '4', '5']]
        update.message.reply_text(
            'Поставьте оценку от 1 до 5',
            reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return 'rating'
        
def registration_rating(update, context):
    context.user_data['registration']['rating'] = int(update.message.text)
    update.message.reply_text('Напишите комментарий, либо нажмите /skip чтобы пропустить')
    return 'comment'