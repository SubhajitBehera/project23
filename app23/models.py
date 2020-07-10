from django.db import models


class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    name =models.CharField(max_length=30)

class AccountInfo(models.Model):
    acno=models.IntegerField(primary_key=True)
    branch=models.CharField(max_length=30)
    ifsc=models.CharField(max_length=30)
    emp=models.OneToOneField(Employee,on_delete=models.CASCADE)