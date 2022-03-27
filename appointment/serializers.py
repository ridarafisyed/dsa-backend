
from rest_framework import serializers
from django.core.mail import send_mail
from  .models import Appointment, Contact


# Appointment Serializer

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields =  (
            "id",
            "name",
            "email",
            "phone",
            "date",
            "time",
        )
    
    def create(self, validated_data):
        appointment = Appointment(
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            date=validated_data['date'],
            time=validated_data['time'],
        )
        subject = "Appointment confirmation"
        date = str(appointment.date)
        time = str(appointment.time)
        message = "Dear " + appointment.name + "You have successfully book the appointment with Dr. Syeda Ali at " + date + " " + time
        send_mail(subject, message, 'samplereciver1234@gmail.com', [appointment.email,'samplereciver1234@gmail.com' ])
        
        appointment.save()
        return appointment




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =  (
            "id",
            "name",
            "email",
            "subject",
            "message",
            "created_at",
        )
        
    
    def create(self, validated_data):
        contact = Contact(
            name=validated_data['name'],
            email=validated_data['email'],
            subject=validated_data['subject'],
            message=validated_data['message'],
        )
       
        send_mail(contact.subject, contact.message, contact.email, ['samplereciver1234@gmail.com', contact.email ])
        
        contact.save()
        
        return contact

