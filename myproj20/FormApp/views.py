from django.shortcuts import render
from.forms import NameForm
from django.http import HttpResponse
from.models import Form
# Create your views here.
def get_name(request):
    if(request.method=='POST'):
        form1=NameForm(request.POST)  #form class object
        if(form1.is_valid()):
            p=Form(name=form1.cleaned_data['name'])
            p.save()
            return HttpResponse("SUCCESS")
    else:
        form1=NameForm()
    return render(request,'base.html',{'form1':form1})


