import logging

from django.core.management import base as management_base, CommandError
from telegram.ext import Updater

from telebaka.utils import get_plugins


class Command(management_base.BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str)
        parser.add_argument('bot_token', type=str)

    def handle(self, *args, app_name, bot_token, **options):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        plugins = get_plugins()
        try:
            updater = Updater(bot_token)
            plugins[app_name].bot.setup(updater.dispatcher)
        except KeyError:
            raise CommandError(f'Module {options["app_name"]} was not found')

        print('Starting polling...')
        if updater.bot.get_webhook_info().url:
            if input('Webhook is set for this token. Continue? [Y/n]') not in ['y', 'Y', '']:
                raise CommandError("Cancelled by user.")
        updater.start_polling(timeout=2)
        updater.idle()
