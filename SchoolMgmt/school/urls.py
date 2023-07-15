from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.home, name='Home'),

    # User Registration
    path('login/', views.login, name="login"),
    path('register/', views.Register.as_view(), name="register"),

    path('add_student/', views.add_student, name='add_student'),
    path('save_student/', views.save_student, name='save_student'),
    path('show_students/', views.show_students, name='show_students'),
    path('student_details/<int:pk>', views.student_details, name='student_details'),
    # path('update_student_details/<int:pk>', views.update_student_details, name='update_student_details'),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),

    #     CRUD Teachers
    path('all_teachers/', views.all_teachers, name='all_teachers'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('show_teacher/<int:pk>', views.show_teacher, name='show_teacher'),
    path('update_teacher/<int:pk>', views.update_teacher, name='update_teacher'),
    path('delete_teacher/<int:pk>', views.delete_teacher, name='delete_teacher'),

    # Department CRUD
    path('add_department/', views.add_department, name='add_department'),
    path('all_departments/', views.all_department, name='all_departments'),
    path('show_department/<int:pk>', views.show_department, name='show_department'),
    path('update_department/<int:pk>', views.update_department, name='update_department'),
    path('delete_department/<int:pk>', views.delete_department, name='delete_department'),

    # Hightlights
    path('add_highlight/', views.add_highlight, name='add_highlight'),
    path('show_highlights/', views.show_highlights, name='show_highlights'),
    path('delete_highlight/<int:pk>', views.delete_highlight, name='delete_highlight'),

]
