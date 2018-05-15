import logging

from telegram import Bot
from telegram.ext import Dispatcher
import lazy_object_proxy

from .models import TelegramBot
from telebaka.utils import get_plugins


def collect_bots():
    dispatchers = {}

    plugins = get_plugins()

    for telegram_bot in TelegramBot.objects.all():
        bot = Bot(telegram_bot.token)
        dispatcher = Dispatcher(bot, None, workers=0)
        try:
            plugins[telegram_bot.plugin_name].bot.setup(dispatcher)
            dispatchers[str(telegram_bot.pk)] = dispatcher
        except KeyError:
            logging.warning(f'Module {telegram_bot.plugin_name} was not found')

    return dispatchers


dispatchers = lazy_object_proxy.Proxy(collect_bots)
