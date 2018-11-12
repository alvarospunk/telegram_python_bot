from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

id_julian = 11949838
id_killo = 66428972
id_alvarospunk = 11644706
id_arubeto = 256150411
id_luli = 172812686
id_javi = 1283123
id_hola = 12381238

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

updater = Updater('462567247:AAEs76XLVZZeTesKJBShttI-XQASUic8yVU')

start
updater.start_polling()
updater.idle()