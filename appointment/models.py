from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField()