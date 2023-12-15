from django.db import models

# Create your models here.
class Reg(models.Model):
    user=models.CharField(primary_key=True,max_length=10)
    pwd=models.CharField(max_length=20)

