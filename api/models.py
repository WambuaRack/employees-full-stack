from django.db import models

class Employee (models.Model):
    name =models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    position=models.CharField(max_length=50)
    salary =models.DecimalField(max_digits=10, decimal_places=2)
    
def __str__(self):
    return self.name

