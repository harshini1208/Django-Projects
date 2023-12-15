import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproj17.settings')
import django
django.setup()
from  CustomerApp.models import Customer
from faker import Faker
fake=Faker()
from random import *

def gen_phoneno():
    s1=randint(7,9)
    num=str(s1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fcid=fake.random_int(min=1,max=999)
        fcname=fake.name()
        fbal=fake.random_int(10000,90000)
        fdob=fake.date()
        femail=fake.email()
        fphoneno=gen_phoneno()
        faddress=fake.address()
        cust_record=Customer.objects.get_or_create(cid=fcid,cname=fcname,bal=fbal,dob=fdob,email=femail,phoneno=fphoneno,address=faddress)
populate(30)