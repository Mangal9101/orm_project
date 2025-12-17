from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    fee=models.IntegerField()
    contact=models.CharField(max_length=13)
    address=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.roll_no} {self.name}'
    
