from django.db import models

# Create your models here.
class Customer(models.Model):
    cid=models.IntegerField()
    cname = models.CharField(max_length=20)
    bal= models.FloatField()
    dob = models.DateField()
    email = models.EmailField()
    phoneno= models.IntegerField()
    address = models.TextField()


