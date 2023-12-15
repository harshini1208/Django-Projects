from django.shortcuts import render
from.models import SimpleInterest

# Create your views here.
def input(request):
    if request.method=='POST':
        p=request.POST['p']
        t = request.POST['t']
        r = request.POST['r']
        si= (int(p)*int(t)*int(r))/100
        s=SimpleInterest(p=p,t=t,r=r,d=si)
        s.save()
        dict={'res':si}

        return render(request,'base1.html',dict)
    return render(request, 'base1.html')


def compute(request):
    r=SimpleInterest.objects.all()
    f={'res':r}
    return render(request,'base2.html',f)



