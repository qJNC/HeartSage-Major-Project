from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class statis(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) 
    age=models.IntegerField()
    gender = models.CharField(max_length=10)
    cp=models.CharField(max_length=10)
    trestbps=models.CharField(max_length=10)
    cholestrol=models.CharField(max_length=10)
    fbs=models.CharField(max_length=10)
    restecg=models.CharField(max_length=10)
    thalach=models.CharField(max_length=10)
    exang=models.CharField(max_length=10)
    oldpeak=models.CharField(max_length=10)
    slope=models.CharField(max_length=10)
    ca=models.CharField(max_length=10)
    thal=models.CharField(max_length=10)

class Doctorsugg(models.Model):
    Doctorname = models.ForeignKey(User, on_delete=models.CASCADE)
    phoneno=models.IntegerField()
    emailid=models.EmailField()
    Address=models.CharField(max_length=1000)
    Status=models.BooleanField(default=False)
    Photo=models.ImageField(upload_to='doctorimages/', blank=True, null=True)
    Designation=models.CharField(max_length=1000 , blank=True, null=True)
    State=models.CharField(max_length=100, blank=True, null=True)

class appoint(models.Model):
    Appointment_CHOICES =  (
        ("Rej", "Rejected"),
        ("Pen", "Pending"),
        ("Conf", "Confirmed"),
        ("Prog", "In Progress"),
        ("Comp", "Completed"),
    )

    
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    dateofappointment=models.DateField(auto_now_add=True)
    timeofappointment=models.CharField(max_length=50 ,null=True)
    doctorname=models.ForeignKey('Doctorsugg', on_delete=models.CASCADE)
    appointmentstatus=models.CharField(max_length=50,choices=Appointment_CHOICES, default="Pen")
    Description=models.CharField(max_length=50,blank=True,null=True)
    

    

