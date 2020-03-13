from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),


]
