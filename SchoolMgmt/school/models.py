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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
