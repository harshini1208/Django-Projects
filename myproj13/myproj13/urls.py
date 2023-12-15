
from django.contrib import admin
from django.urls import path,re_path
from StaticApp import views

urlpatterns = [
    path('admin/', admin.site.urls)
    re_path(r'StaticApp^$',views.input)
]
