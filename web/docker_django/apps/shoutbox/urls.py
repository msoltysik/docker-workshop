from django.core.mail import send_mail
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
