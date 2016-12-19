from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^selenium1', views.selenium_hatena, name='index'),
]
