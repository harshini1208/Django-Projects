from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime
def input(request):
    date=datetime.datetime.now()
    return HttpResponse("<html><body bgcolor='red' text='yellow'><b><h1>Todays Date and Time is:" +str(date)+"</h1></b></body></html>")

