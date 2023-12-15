
from.import views#here . indicates within same folder
from django.urls import re_path
#from SampleApp import views
urlpatterns=[
    re_path(r'^samp$',views.input1),   #note:we can specify any no of urls
    re_path(r'^test$',views.input1),


]