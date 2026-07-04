from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('students/', views.student_list, name='student_list'),
]
