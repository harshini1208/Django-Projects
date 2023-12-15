from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def employee(request):
    str1='''
         <html>
         <body bgcolor='yellow' text='red'>
         <center>
         <table border=5>
         <caption><h1><b><u>EMPLOYEE DETAILS</h1></b></u></caption>
         <tr>
         <th>EMPID</th>
         <th>EMPNAME</th>
         <th>SALARY</th>
         <th>DESIGNATION</th>
         </tr>  
         <tr>
         <td>102</td>
         <td>Harshini</td>
         <td>50000</td>
         <td>Software Developer</td>
         </tr>
         <tr>
         <td>103</td>
         <td>uday</td>
         <td>40000</td>
         <td> Manager</td>
         </tr>
         <tr>
         <td>104</td>
         <td>Nikita</td>
         <td>60000</td>
         <td>Business Analyst</td>
         </tr>
         </table>
         </body>
         <html>
         
    '''
    return HttpResponse(str1)


def customer(request):
    str1 = '''
         <html>
         <body bgcolor='red' text='black'>
         <center>
         <table border=5>
         <caption><h1><b><u>CUSTOMER DETAILS</h1></b></u></caption>
         <tr>
         <th>CUSTID</th>
         <th>CUSTNAME</th>
         <th>DUEAMOUNT</th>
         <th>LOCATION</th>
         </tr>
         <tr>
         <td>100</td>
         <td>Harshini</td>
         <td>10000</td>
         <td>Dilsukhnagar</td>
         </tr>
         <tr>
         <td>101</td>
         <td>uday</td>
         <td>20000</td>
         <td> Madhapur</td>
         </tr>
         <tr>
         <td>102</td>
         <td>Nikita</td>
         <td>15000</td>
         <td>Miyapur</td>
         </tr>
         </table>
         </body>
         <html>

    '''
    return HttpResponse(str1)

def student(request):
    str1 = '''
         <html>
         <body bgcolor='red' text='black'>
         <center>
         <table border=5>
         <caption><h1><b><u>STUDENT DETAILS</h1></b></u></caption>
         <tr>
         <th>STDID</th>
         <th>STDNAME</th>
         <th>BRANCH</th>
         <th>PERCENTAGE</th>
         </tr>
         <tr>
         <td>500</td>
         <td>Harshini</td>
         <td>CSE</td>
         <td>92%</td>
         </tr>
         <tr>
         <td>501</td>
         <td>uday</td>
         <td>ECE</td>
         <td> 70%</td>
         </tr>
         <tr>
         <td>502</td>
         <td>Nikita</td>
         <td>EEE</td>
         <td>80%</td>
         </tr>
         </table>
         </body>
         <html>

    '''
    return HttpResponse(str1)
