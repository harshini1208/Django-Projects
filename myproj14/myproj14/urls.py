
from django.contrib import admin
from django.urls import path,re_path
from NewsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^NewsApp$',views.input)
]
