from django.shortcuts import render
from.forms import ContactForm
from.forms import ContactForm1

# Create your views here.
def input(request):
    if(request.method=='POST'):
        form=ContactForm(request.POST)  #bounded form
        if(form.is_valid()):
            #now capturing the fields
             name=form.cleaned_data['name']
             email = form.cleaned_data['email']
             city= form.cleaned_data['city']
             address = form.cleaned_data['address']
             print(name,email,city,address)
    form=ContactForm()  #empty
    return render(request,'base.html',{'form':form})

def input_details(request):
    if(request.method=='POST'):
        form=ContactForm1(request.POST)  #bounded form
        if(form.is_valid()):
            form.save()
            print('VALID')
    form=ContactForm1()
    return render(request,'base.html',{'form':form})