from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='employee_photos', null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"