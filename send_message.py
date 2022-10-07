import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    bot.send_message(chat_id=id_alvarospunk, text="Hola alvarito")

updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'])

start
updater.start_polling()
updater.idle()
