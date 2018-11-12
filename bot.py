from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)

updater = Updater('462567247:AAEs76XLVZZeTesKJBShttI-XQASUic8yVU')


from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
