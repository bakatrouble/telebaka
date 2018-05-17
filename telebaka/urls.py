from django.contrib import admin
from django.urls import path, include

from bots.views import WebhookView

urlpatterns = [
    path('bots/', include('bots.urls', namespace='bots')),
    path('webhook/<pk>/', WebhookView.as_view()),
    path('admin/', admin.site.urls),
]
