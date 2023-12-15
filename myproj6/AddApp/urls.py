
from django.urls import path,re_path
from AddApp import views

urlpatterns = [
    re_path(r'^$',views.input),
    re_path(r'Add$',views.add)

]