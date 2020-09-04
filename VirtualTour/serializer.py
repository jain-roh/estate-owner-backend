from rest_framework import serializers
import re
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import VirtualTour
from Property.models import Property
from User.models import Buyer,Seller

class VirtualTourSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    buyer = serializers.PrimaryKeyRelatedField(queryset=Buyer.objects.all())
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    property=serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())
    datetime = serializers.DateTimeField()
    class Meta:
        model = VirtualTour
        fields = '__all__'

    def create(self, validated_data):
        return VirtualTour.objects.create(**validated_data)


