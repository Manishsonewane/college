from django.db import models

# Create your models here.
class reg(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    over18=models.BooleanField()
    DOB=models.DateField()
    email=models.EmailField()
    username=models.CharField(max_length=20)
    createpass=models.CharField(max_length=20)
    confirmpass=models.CharField(max_length=20)