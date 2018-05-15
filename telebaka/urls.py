from django.contrib import admin
from django.urls import path

from bots.views import WebhookView

urlpatterns = [
    path('webhook/<pk>/', WebhookView.as_view()),
    path('admin/', admin.site.urls),
]
