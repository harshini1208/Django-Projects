from django.urls import path
from .import views

urlpatterns = [
    path('',views.taskapp, name='taskapp'),
    path('temp',views.temp,name='temp'),
    ]