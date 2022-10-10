import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

csv = "https://docs.google.com/spreadsheets/d/e/" + os.environ['CSV_ID'] + "/pub?output=csv"

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def answer(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="No contesto a tonterias")

updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'])

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))

updater.start_polling()
updater.idle()

