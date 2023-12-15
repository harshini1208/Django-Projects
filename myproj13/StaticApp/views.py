from django.shortcuts import render
import datetime

# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    hour=float(dt.strftime("%H"))
    msg="HELLO....HYDERABAD!!!"
    msg2="THE CURRENT DATE AND TIME IS:{}"
    if(hour<12):
        msg=msg+"Very Good Morning!!"+msg2.format(str(dt))
    elif(hour<16.00):
        msg = msg + "Very Good Afternoon!!" + msg2.format(str(dt))
    elif(hour<20.00):
        msg = msg + "Very Good Evening!!" + msg2.format(str(dt))
    else:
        msg = msg + "Very Good Night!!" + msg2.format(str(dt))
    dict={'message':msg,"date":dt}
    return render(request,"base.html",dict)



