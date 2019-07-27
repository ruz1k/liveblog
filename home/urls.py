from django.conf.urls import url
from home.views import HomeView
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)