from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.urls import reverse
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'main/home.html', {})


def students(request):
    students = Student.objects.filter(is_active=True)
    return render(request, 'main/students.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'main/student_detail.html', {'student': student})


def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'main/student_add.html', {'form': form})


def student_edit(request, pk):
    post = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=post)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=post.pk)
    else:
        form = StudentForm(instance=post)
    return render(request, 'main/student_edit.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.is_active = False
        student.save()
        return redirect('students')
    return HttpResponseRedirect(reverse('students'))


def lockers(request):
    return render(request, 'main/lockers.html', {})


def locker_groups(request):
    return render(request, 'main/locker_groups.html', {})
