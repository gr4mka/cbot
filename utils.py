import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
from telegram import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(filename="bot.log", level=logging.INFO)

def main_keyboard():
    return ReplyKeyboardMarkup([['Registration'], ['Menu'], ['About']])
    