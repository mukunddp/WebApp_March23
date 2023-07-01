from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='Home'),
    path('home_http/', views.home_http, name='HTTP'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add_student/', views.add_student, name='add_student'),
    path('save_student/', views.save_student, name='save_student'),

]
