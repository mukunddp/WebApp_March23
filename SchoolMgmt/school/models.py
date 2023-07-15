from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class Teachers(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subjects = models.CharField(max_length=500)
    address = models.TextField()
    age = models.IntegerField()
    dob = models.DateTimeField()
    mobile_no = models.BigIntegerField()
    qualification = models.CharField(max_length=500)
    designation = models.CharField(max_length=100)
    department = models.ForeignKey('school.Departments', on_delete=models.CASCADE)


class Departments(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hod = models.CharField(max_length=100)


class Highlights(models.Model):
    name = models.CharField(max_length=500)
    link = models.TextField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
