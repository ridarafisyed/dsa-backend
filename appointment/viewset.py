from rest_framework import  viewsets, permissions

from rest_framework import generics, permissions
from .serializers import AppointmentSerializer, ContactSerializer
from django.core.mail import send_mail
from .models import Appointment, Contact


class AppointmentViewset(viewsets.ModelViewSet):
    
    queryset = Appointment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppointmentSerializer


class ContactViewset(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer
