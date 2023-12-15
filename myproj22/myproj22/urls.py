
from django.contrib import admin
from django.urls import path,re_path
from RegandLoginApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.home),
    re_path(r'^register$',views.register),
    re_path(r'^login$',views.login)
]
