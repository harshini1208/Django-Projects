
from django.contrib import admin
from django.urls import path,re_path
from MultiViewApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^emp$",views.employee),
    re_path(r"^cust$",views.customer),
    re_path(r"^std$",views.student),

]
