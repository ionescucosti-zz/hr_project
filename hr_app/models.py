from django.db import models


class Employees(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(null=True, max_length=30)
    gender = models.CharField(null=True, max_length=10)
    date_of_birth = models.DateField(null=True)
    industry = models.CharField(null=True, max_length=50)
    salary = models.IntegerField(null=True)
    years_of_experience = models.IntegerField(null=True)

