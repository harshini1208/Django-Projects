from django.urls import path
from .import views

urlpatterns = [
    path('',views.modelapp, name='modelapp'),
    ]