from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('lockers/', views.lockers, name='lockers'),
    path('locker-groups/', views.locker_groups, name='locker_groups'),
]
