from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def input(request):
    return HttpResponse("<html><body bgcolor='red' text='yellow'><b><h1>WELCOME TO DJANGO WORLD!!!</b></h1></body></html>")


