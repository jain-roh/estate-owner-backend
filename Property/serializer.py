from rest_framework import serializers
import re
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Property

class PropertySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name = serializers.CharField(max_length=200, allow_null=True)
    latitude = serializers.FloatField(allow_null=True)
    longitude = serializers.FloatField(allow_null=True)
    price = serializers.FloatField(validators=[MinValueValidator(1, 00)], default=1.00)
    beds = serializers.FloatField(validators=[MinValueValidator(0, 00)], default=1.00)
    bath = serializers.FloatField(validators=[MinValueValidator(0, 99)], default=1.00)
    size = serializers.FloatField(validators=[MinValueValidator(10, 00)], default=1.00)
    description = serializers.CharField(max_length=1000, allow_null=True)
    CHOICES = [('residential', 'Residential'),
               ('commercial', 'Commercial')]
    propertytype = serializers.ChoiceField(
        choices=CHOICES,
        default='residential')
    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        return Property.objects.create(**validated_data)