from django.shortcuts import render
import math

# Create your views here.
def input(request):
    return render(request,'base1.html')

# def compute(request):
#     x=float(request.GET['t1']),
#     dict1={'res':math.sqrt(x)},
#     return render(request,'base2.html',dict1)
#or return render(request,'base2.html',dict1)
#or return render(request,'base2.html',{'res':math.sqrt(x))
def compute(request):
# Get the value of 't1' from the request's GET parameters
    t1 = float(request.GET.get('t1'))

    # Check if t1 is a valid number
    if isinstance(t1, (int, float)):
            # Calculate the square root
        result = math.sqrt(t1)

            # Create a dictionary to pass to the template
        dict1 = {'res': result}

            # Render the template with the result
        return render(request, 'base2.html', dict1)
