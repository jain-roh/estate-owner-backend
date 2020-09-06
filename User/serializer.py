from rest_framework import serializers
import re
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Buyer,Seller

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username=serializers.CharField(max_length=10,min_length=5,allow_blank=False,allow_null=False)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50,min_length=8,allow_blank=False,allow_null=False)
    is_staff=serializers.BooleanField()

    class Meta:
        model = User
        fields = ['id','username','email','is_staff']
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        """
        Check that start is before finish.
        """
        return data

class BuyerSerializer(UserSerializer):
    id = serializers.ReadOnlyField()
    location = serializers.CharField(allow_blank=False,allow_null=True,default=None)
    middle_name = serializers.CharField(allow_null=True,default=None)

    class Meta:
        model = Buyer
        fields = '__all__'

    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        pwd = validated_data.pop('password')
        validated_data['is_staff'] = False
        buyr = Buyer.objects.create(**validated_data)
        try:
            buyr.set_password(pwd)
            buyr.save()

        except Exception as e:
            buyr.delete()
        print(buyr)
        return buyr

class SellerSerializer(UserSerializer):
    id = serializers.ReadOnlyField()
    description = serializers.CharField(max_length=1000, allow_null=True,default=None)
    location = serializers.CharField(allow_blank=True,allow_null=True,default=None)
    middle_name = serializers.CharField(allow_null=True,default=None)
    phone_number = serializers.IntegerField(allow_null=True,default=None)
    class Meta:
        model = Seller
        fields = '__all__'

    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        pwd = validated_data.pop('password')
        validated_data['is_staff'] = True
        sllr = Seller.objects.create(**validated_data)
        try:
            sllr.set_password(pwd)
            sllr.save()

        except Exception as e:
            sllr.delete()
        print(sllr)
        return sllr