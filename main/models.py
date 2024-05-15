from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    matricula = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Locker(models.Model):
    number = models.IntegerField()
    number_of_doors = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.number)


class Door(models.Model):
    number = models.IntegerField()
    identifier = models.CharField(max_length=10)
    locker = models.ForeignKey(Locker, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.identifier
