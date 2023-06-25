from django.shortcuts import render, HttpResponse


# Create your views here. # Logic
def home(request):
    return render(request, 'home.html')


def home_http(request):
    return HttpResponse('This is HTTP Response')
