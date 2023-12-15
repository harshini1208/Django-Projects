
from django.contrib import admin
from django.urls import path,re_path
from SampleApp import views as v1
from TestApp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^sample$',v1.input1),
    re_path(r'^test$',v2.input2)
]
