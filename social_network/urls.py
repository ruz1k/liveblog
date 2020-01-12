from django.conf.urls import url
from social_network.views import SocialView
from . import views

urlpatterns = [
    url(r'^$', SocialView.as_view(), name='social'),
]
