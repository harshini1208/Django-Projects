from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=30)
    published_year=models.DateField()
    price=models.FloatField()

    def __str__(self):
        return self.validate_unique()
