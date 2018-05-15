from uuid import uuid4
from django.db import models


class TelegramBot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    plugin_name = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
    url_prefix = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.url_prefix:
            self.url_prefix = None
        return super(TelegramBot, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return '{} [#{}]'.format(self.plugin_name, self.pk)


class BotAdminUser(models.Model):
    name = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)

    def __str__(self):
        return '{} [chat_id: {}]'.format(self.name, self.chat_id)
