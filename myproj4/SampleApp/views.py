from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input1(request):
    return HttpResponse("<html><body bgcolor='yellow' text='red'><h1>Welcome To Python World!!!</h1></body></html>")
