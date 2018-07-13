from telegram import Bot, Update, MessageEntity
from telegram.ext import Dispatcher, MessageHandler, Filters


def message(bot: Bot, update: Update):
    print(update.message.text)
    update.message.forward(update.message.chat_id)


def setup(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.all, message))
    return dispatcher
