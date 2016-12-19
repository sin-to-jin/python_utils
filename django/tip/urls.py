from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^selenium_hatena_profile', views.selenium_hatena_profile, name='index'),
]
