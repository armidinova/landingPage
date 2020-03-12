from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name = 'home' ),
    #path('landing/', views.landing, name = 'landing' ),
    path('add/', views.add, name = 'add' ),
    path('delete/', views.delete, name = 'delete' ),
]