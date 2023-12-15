from django.db import models

# Create your models here.
class Sales(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=20)
    price=models.FloatField()
    mfgdate=models.DateField()