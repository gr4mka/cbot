from telegram import ParseMode, ReplyKeyboardMarkup, ReplyKeyboardRemove
from db import db, get_or_create_user, save_reg
from telegram.ext.conversationhandler import ConversationHandler
#from utils import main_keyboard

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
        reply_keyboard = [['тык1', 'тык2', 'тык3', 'тык4', 'тык5']]
        update.message.reply_text(
            'Выберите интересующий Вас пункт',
            reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return 'choice'
        
def registration_choice(update, context):
    context.user_data['registration']['choice'] = str(update.message.text)
    update.message.reply_text('Напишите комментарий, либо нажмите /skip чтобы пропустить')
    return 'comment'

def registration_comment(update, context):
    context.user_data['registration']['comment'] = update.message.text
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    save_reg(db, user['user_id']), context.user_data['registration']
    user_text = f"""<b> Имя Фамилия</b>: {context.user_data['registration']['name']}
<b>Выбор</b>: {context.user_data['registration']['choice']}
<b>Комментарий</b>: {context.user_data['registration']['comment']}
"""
    update.message.reply_text(user_text, parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def registration_skip(update, context):
    user = get_or_create_user(db, update.effective_user, update.message.chat.id)
    save_reg(db, user['user_id']), context.user_data['registration']
    user_text = f"""<b> Имя Фамилия</b>: {context.user_data['registration']['name']}
<b>Выбор</b>: {context.user_data['registration']['choice']}
"""
    update.message.reply_text(user_text, parse_mode=ParseMode.HTML)
    return ConversationHandler.END

def registration_mistake(update, context):
    update.message.reply_text('Введены некорректрые данные. Попробуйте еще раз')