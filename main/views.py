from django.shortcuts import render
from .models import Student


def home(request):
    students = Student.objects.filter(is_active=True)
    return render(request, 'main/home.html', {'students': students})
