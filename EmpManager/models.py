from django.db import models

class EmployeeRecord(models.Model):
    empid=models.IntegerField(default=0)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.CharField(max_length=100)
    department=models.CharField(max_length=20)
    salary=models.IntegerField(default=0)
    picture=models.ImageField(upload_to='media')

    def __str__(self):
        return self.empid