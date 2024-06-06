from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    position = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    added_date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Worker(models.Model):
    ATTENDANCE_CHOICES = [
        ('full_time', 'Full Time'),
        ('half_time', 'Half Time'),
        ('leave', 'Leave'),
        
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    attendance_date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username