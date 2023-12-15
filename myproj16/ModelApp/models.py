from django.db import models

# Create your models here.
class Emp(models.Model):
    eno=models.Intergerfield()
    ename=models.Charfield(max_length=20)
    sal=models.Floatfield()
    sex=models.Charfield(max_length=6)
    dno=models.Intergerfield()
    # def __str__(self):
    #     return self.ename