from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
#from rest_framework.views import APIView

# Create your views here.
class Sample(View):
    def get(self,request):
        return render(request,'base.html')

class Add(View):
    def post(self,request):
        x=int(request.POST['t1'])
        y=int(request.POST['t2'])
        z=str(x+y)
        return HttpResponse("<html><body bgcolor='red'><h1>SUM IS:"+z+"</h1></body></html>")
