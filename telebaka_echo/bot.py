import logging

from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def message(bot: Bot, update: Update):
    update.message.forward(update.message.chat_id)


def setup(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text, message))
    return dispatcher
