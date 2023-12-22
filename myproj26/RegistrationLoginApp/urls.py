from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    path('login',views.Login_user),
    path('registration',views.Register_user),
    path('logout',views.Logout_user),

]