from django.contrib import admin
from django.urls import path
from .views import Sample,Add

urlpatterns = [
    path('sample',Sample.as_view()),
    path('Add',Add.as_view()),
]