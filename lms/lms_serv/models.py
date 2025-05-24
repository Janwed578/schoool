from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=70)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
