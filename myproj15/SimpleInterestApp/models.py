from django.db import models

# Create your models here.
class SimpleInterest(models.Model):
    p=models.CharField(max_length=200)
    t=models.CharField(max_length=200)
    r=models.CharField(max_length=200)
    d=models.CharField(max_length=200)
