from django.shortcuts import render, HttpResponse, redirect
from .models import Student


# Create your views here. # Logic
def home(request):
    return render(request, 'home.html')


def home_http(request):
    return HttpResponse('This is HTTP Response')


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def add_student(request):
    return render(request, 'add_student.html')


# Create Operation
def save_student(request):
    s = Student()
    s.name = request.POST.get('name')
    s.email = request.POST.get('email')
    s.address = request.POST.get('address')
    s.age = request.POST.get('age')
    s.mobile_no = request.POST.get('mobile')
    s.dob = request.POST.get('dob')
    s.class_name = request.POST.get('class_name')
    s.roll_no = request.POST.get('roll_no')
    s.save()
    print('Successfully Added Data In Database')
    # save will add the changes inside the model
    return redirect('add_student')


# Retrieve Operation
def show_students(request):

    return
