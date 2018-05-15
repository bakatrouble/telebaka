from django.core.management import base as management_base
from django.conf import settings

from bots.bots import dispatchers


class Command(management_base.BaseCommand):
    def handle(self, *args, **options):
        for pk, dispatcher in dispatchers.items():
            dispatcher.bot.set_webhook(f'https://{settings.WEBHOOK_DOMAIN}/webhook/{pk}/')
        print('Webhooks set')
