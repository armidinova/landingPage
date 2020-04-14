from django.conf.urls import url
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^checkout/$', views.checkout, name='checkout'),


]
