from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

csv = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTDOxVghsVJHNekUk0YQ-2hlC3-VBWq8eCIFTAsST6_3f7bwG7ZjRzb26crm8fw_6L9ypGwN1_B6QfV/pub?output=csv"

id_julian = 11949838
id_killo = 66428972
id_alvarospunk = 11644706
id_arubeto = 256150411
id_luli = 172812686

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def answer(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="No contesto a tonterias")

updater = Updater('462567247:AAEs76XLVZZeTesKJBShttI-XQASUic8yVU')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, answer))

updater.start_polling()
updater.idle()

