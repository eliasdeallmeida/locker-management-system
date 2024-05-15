from django import forms
from .models import Student, Locker, Door


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'matricula')


class LockerForm(forms.ModelForm):
    class Meta:
        model = Locker
        fields = ('number', 'number_of_doors')


class DoorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoorForm, self).__init__(*args, **kwargs)
        self.fields['locker'].queryset = Locker.objects.filter(is_active=True)
        self.fields['student'].queryset = Student.objects.filter(is_active=True)

    class Meta:
        model = Door
        fields = ('number', 'identifier', 'locker', 'student')
