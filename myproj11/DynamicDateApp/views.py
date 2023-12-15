from django.shortcuts import render
import datetime

# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    dict1={'date':dt}
    return render(request,'base.html',context=dict1)


