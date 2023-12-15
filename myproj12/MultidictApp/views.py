from django.shortcuts import render

# Create your views here.
import datetime
def input(request):
    date=datetime.datetime.now()
    day=date.strftime("%A")
    month=date.strftime("%B")
    year=date.strftime("%Y")
    dict={'date':date,'cur_day':day,'cur_month':month,'cur_year':year}
    return render(request,'base.html',context=dict)