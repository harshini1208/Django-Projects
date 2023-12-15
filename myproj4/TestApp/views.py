from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def input2(request):
    return HttpResponse("<html><body bgcolor='blue' text='black'><h1>Welcome To Django World!!!!</h1></body></html>")
