from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.home, name='Home'),
    path('home_http/', views.home_http, name='HTTP'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add_student/', views.add_student, name='add_student'),
    path('save_student/', views.save_student, name='save_student'),
    path('show_students/', views.show_students, name='show_students'),
    path('student_details/<int:pk>', views.student_details, name='student_details'),
    # path('update_student_details/<int:pk>', views.update_student_details, name='update_student_details'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),

]
