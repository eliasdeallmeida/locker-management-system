from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Locker, Door
from .forms import StudentForm, LockerForm, DoorForm
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
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'main/student_edit.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.is_active = False
        student.save()
        return redirect('students')
    return HttpResponseRedirect(reverse('students'))


def lockers(request):
    lockers = Locker.objects.filter(is_active=True)
    return render(request, 'main/lockers.html', {'lockers': lockers})


def locker_detail(request, pk):
    locker = get_object_or_404(Locker, pk=pk)
    return render(request, 'main/locker_detail.html', {'locker': locker})


def locker_add(request):
    if request.method == "POST":
        form = LockerForm(request.POST)
        if form.is_valid():
            locker = form.save(commit=False)
            locker_number = form.cleaned_data['number']
            number_of_doors = form.cleaned_data['number_of_doors']
            locker.save()
            for door_number in range(1, number_of_doors + 1):
                identifier = f'{number_of_doors:02}-{locker_number:03}-{door_number:02}'
                Door.objects.create(number=door_number, identifier=identifier, locker=locker)
            return redirect('locker_detail', pk=locker.pk)
    else:
        form = LockerForm()
    return render(request, 'main/locker_add.html', {'form': form})


def locker_edit(request, pk):
    locker = get_object_or_404(Locker, pk=pk)
    if request.method == "POST":
        form = LockerForm(request.POST, instance=locker)
        if form.is_valid():
            locker = form.save(commit=False)
            locker.save()
            return redirect('locker_detail', pk=locker.pk)
    else:
        form = LockerForm(instance=locker)
    return render(request, 'main/locker_edit.html', {'form': form})


def locker_delete(request, pk):
    locker = get_object_or_404(Locker, pk=pk)
    if request.method == 'POST':
        Door.objects.filter(locker=locker).update(is_active=False)
        locker.is_active = False
        locker.save()
        return redirect('lockers')
    return HttpResponseRedirect(reverse('lockers'))


def doors(request):
    doors = Door.objects.filter(is_active=True)
    return render(request, 'main/doors.html', {'doors': doors})


def door_detail(request, pk):
    door = get_object_or_404(Door, pk=pk)
    return render(request, 'main/door_detail.html', {'door': door})


def door_edit(request, pk):
    door = get_object_or_404(Door, pk=pk)
    if request.method == "POST":
        form = DoorForm(request.POST, instance=door)
        if form.is_valid():
            door = form.save(commit=False)
            if form.cleaned_data['student']:
                door.is_occupied = True
            else:
                door.is_occupied = False
            door.save()
            return redirect('door_detail', pk=door.pk)
    else:
        form = DoorForm(instance=door)
    return render(request, 'main/door_edit.html', {'form': form})
