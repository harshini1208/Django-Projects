


from django.contrib import admin
from django.urls import path,re_path
from DemoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^demo$',views.input)
]
