from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('', views.home, name='home'),
    
    # Students
    path('students/', views.students, name='students'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    # Lockers
    path('lockers/', views.lockers, name='lockers'),
    path('lockers/<int:pk>/', views.locker_detail, name='locker_detail'),
    path('lockers/add/', views.locker_add, name='locker_add'),
    path('lockers/edit/<int:pk>/', views.locker_edit, name='locker_edit'),
    path('lockers/delete/<int:pk>/', views.locker_delete, name='locker_delete'),

    # Doors
    path('doors/', views.doors, name='doors'),
    path('door/<int:pk>', views.door_detail, name='door_detail'),
    path('door/edit/<int:pk>', views.door_edit, name='door_edit'),
]
