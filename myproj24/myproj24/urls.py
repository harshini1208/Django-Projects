
from django.contrib import admin
from django.urls import path,re_path
from crispyApp  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.input),
    re_path(r'^contact$',views.input_details)

]
