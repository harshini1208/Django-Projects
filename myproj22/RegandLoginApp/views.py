from django.shortcuts import render
from django.http import HttpResponse
from.models import Reg
from.forms import LoginForm
from.forms import RegForm

# Create your views here.
def home(request):
    return  render(request,'home.html')

def register(request):
    if(request.method=='POST'):
        form=RegForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponse("Registration Successfull!!!")
        else:
            print(form.errors)
    else:
        form=RegForm()
    return render(request,'register.html',{'form':form})
def login(request):
    if(request.method=='POST'):
        form1=LoginForm(request.POST)
        if(form1.is_valid()):
            user=form1.cleaned_data['user']
            pwd=form1.cleaned_data['pwd']
            dbuser=Reg.objects.filter(user=user,pwd=pwd)
            if(not dbuser):
                return HttpResponse('LOGIN FAILED')
            else:
                return HttpResponse("LOGIN SUCCESSFULL!!!")
    else:
        form1=LoginForm()
    return render(request,'login.html',{'form':form1})

