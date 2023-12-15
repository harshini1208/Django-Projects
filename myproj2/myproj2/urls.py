
from django.contrib import admin
from django.urls import path,re_path
from DateApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^date$',views.input)
]
