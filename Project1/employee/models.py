from django.db import models


class Employee(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.emp_name}"
