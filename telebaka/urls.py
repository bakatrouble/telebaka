from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bots.views import WebhookView
from telebaka import settings

urlpatterns = [
    path('bots/', include('bots.urls', namespace='bots')),
    path('webhook/<pk>/', WebhookView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

