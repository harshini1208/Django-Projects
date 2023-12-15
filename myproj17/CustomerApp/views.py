from django.shortcuts import render

# Create your views here.
from .models import Customer
def Customer_input(request):
    #customer=Customer.objects.all()
    #customer=Customer.objects.filter(bal__lt=40000)
    #customer = Customer.objects.filter(cname__startswith='A')
    #customer = Customer.objects.all().order_by('-bal')
    #customer = Customer.objects.filter(cname__startswith='A',bal__lt=40000)
    customer = Customer.objects.filter(cname='Angela Flowers')



    return render(request,'base.html',{'customer':customer})