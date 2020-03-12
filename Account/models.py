from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contactno = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=30,unique=True)

class LoginModel(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
