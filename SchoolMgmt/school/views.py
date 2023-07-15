from django.shortcuts import render, HttpResponse, redirect
from .models import Student, UserRegisterForm, Teachers, Departments, Highlights
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


# Create your views here. # Logic
def home(request):
    return render(request, 'home.html')


# Register User
class Register(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def login(request):
    return HttpResponseRedirect("/accounts/login")


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
    return redirect('show_students')


# Retrieve Operation / Read
def show_students(request):
    students_data = Student.objects.all()
    return render(request, 'all_student_data.html', {'students_data': students_data})


def student_details(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'student_details.html', {'student': student})


# UPDATE Operation
# def update_student_details(request, pk):
#     student = Student.objects.get(id=pk)
#     return render(request, 'update_student_details.html', {'student': student})


def update_student(request, pk):
    s = Student.objects.get(id=pk)
    if request.method == "POST":
        s.name = request.POST.get('name')
        s.email = request.POST.get('email')
        s.address = request.POST.get('address')
        s.age = request.POST.get('age')
        s.mobile_no = request.POST.get('mobile')
        # s.dob = request.POST.get('dob')
        s.class_name = request.POST.get('class_name')
        s.roll_no = request.POST.get('roll_no')
        s.save()
        print('Successfully Updated Data In Database')
        # save will add the changes inside the model
        return redirect('show_students')
    return render(request, 'update_student_details.html', {'student': s})


# Delete Operation
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    print('Successfully Deleted Data In Database')
    return redirect('show_students')


# CRUD Teachers
def add_teacher(request):
    d = Departments.objects.all()
    if request.method == 'POST':
        t = Teachers()
        t.name = request.POST.get('name')
        t.email = request.POST.get('email')
        t.subjects = request.POST.get('subjects')
        t.address = request.POST.get('address')
        t.age = request.POST.get('age')
        t.dob = request.POST.get('dob')
        t.mobile_no = request.POST.get('mobile_no')
        t.qualification = request.POST.get('qualification')
        t.designation = request.POST.get('designation')
        department_id = request.POST.get('department')
        d = Departments.objects.get(id=department_id)
        t.department = d
        t.save()
        return redirect('all_teachers')
    return render(request, 'teachers/add_teacher.html', {'departments': d})


def all_teachers(request):
    t = Teachers.objects.all()
    return render(request, 'teachers/all_teachers.html', {'all_teachers': t})


def show_teacher(request, pk):
    t = Teachers.objects.get(id=pk)
    return render(request, 'teachers/show_teacher.html', {'teacher': t})


def update_teacher(request, pk):
    t = Teachers.objects.get(id=pk)
    if request.method == 'POST':
        t.name = request.POST.get('name')
        t.email = request.POST.get('email')
        t.subjects = request.POST.get('subjects')
        t.address = request.POST.get('address')
        t.age = request.POST.get('age')
        t.dob = request.POST.get('dob')
        t.mobile_no = request.POST.get('mobile_no')
        t.qualification = request.POST.get('qualification')
        t.designation = request.POST.get('designation')
        department_id = request.POST.get('department')
        d = Departments.objects.get(id=department_id)
        t.department = d
        t.save()
        return redirect('all_teachers')
    return render(request, 'teachers/update_teacher.html', {'teacher': t})


def delete_teacher(request, pk):
    t = Teachers.objects.get(id=pk)
    t.delete()
    return redirect('all_teachers')


# CRUD Department
def add_department(request):
    if request.method == 'POST':
        d = Departments()
        d.name = request.POST.get('name')
        d.description = request.POST.get('description')
        d.hod = request.POST.get('hod')
        d.save()
        return redirect('all_departments')
    return render(request, 'department/add_department.html')


def all_department(request):
    d = Departments.objects.all()
    return render(request, 'department/all_department.html', {'departments': d})


def show_department(request, pk):
    d = Departments.objects.get(id=pk)
    return render(request, 'department/show_department.html', {'department': d})


def update_department(request, pk):
    d = Departments.objects.get(id=pk)
    if request.method == 'POST':
        d.name = request.POST.get('name')
        d.description = request.POST.get('description')
        d.hod = request.POST.get('hod')
        d.save()
        return redirect('all_departments')
    return render(request, 'department/update_department.html', {'department': d})


def delete_department(request, pk):
    d = Departments.objects.get(id=pk)
    d.delete()
    return redirect('all_departments')


# CRUD Highlights
def add_highlight(request):
    if request.method == 'POST':
        h = Highlights()
        h.name = request.POST.get('name')
        h.name = request.POST.get('name')
        h.save()
        return redirect('show_highlights')
    return render(request, 'highlights/add_highlight.html')


def show_highlights(request):
    h = Highlights.objects.all()
    return render(request, 'highlights/show_highlights.html', {'highlights': h})


def delete_highlight(request, pk):
    h = Highlights.objects.get(id=pk)
    h.delete()
    return redirect('show_highlights')
