import json
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from jsonview.decorators import json_view
from telegram import Update

from bots.bots import dispatchers


class WebhookView(View):
    @method_decorator(json_view)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhookView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, pk, **kwargs):
        dispatcher = dispatchers[pk]
        dispatcher.process_update(Update.de_json(json.loads(request.body), dispatcher.bot))
        return {}
