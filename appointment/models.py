from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name