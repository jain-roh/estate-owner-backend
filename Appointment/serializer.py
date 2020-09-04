from rest_framework import serializers
import re
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Appointment
from Property.models import Property
from User.models import Buyer,Seller

class AppointmentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    buyer = serializers.PrimaryKeyRelatedField(queryset=Buyer.objects.all())
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    property=serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())
    datetime = serializers.DateTimeField()
    CHOICES = [
                ('accept', 'Accept'),
               ('reschedule', 'Reschedule'),
               ('reject', 'Reject')]
    response = serializers.ChoiceField(
        choices=CHOICES,
        default=None,
        allow_null=True    )
    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        appointment = Appointment.objects.get(pk=instance.id)
        Appointment.objects.filter(pk=instance.id) \
            .update(**validated_data)
        return appointment
