from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='Home'),
    path('home_http/', views.home_http, name='HTTP')
]