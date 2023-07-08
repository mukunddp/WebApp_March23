from django.db import models


# ORMs : Object Relation Mappers
# Create your models here.  DataBase
class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.TextField()
    age = models.IntegerField()
    dob = models.DateTimeField()
    mobile_no = models.BigIntegerField()
    roll_no = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
