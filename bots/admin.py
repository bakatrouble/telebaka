from django.contrib import admin
from django.forms import ChoiceField

from telebaka.utils import get_plugins

from .models import BotAdminUser, TelegramBot


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(TelegramBotAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['plugin_name'] = ChoiceField(choices=[(pname, pname) for pname in get_plugins().keys()])
        return form
