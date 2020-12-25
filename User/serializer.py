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
        fields = ['id','username','email','is_staff''first_name','last_name','profile_pic']
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
    profile_pic=serializers.ImageField(allow_null=True,default=None)
    first_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False, allow_null=False)

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
            print(buyr)

        except Exception as e:
            print(e)
            buyr.delete()

        return buyr
    def update(self, instance,validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        pwd = validated_data.pop('password')
        if validated_data.get('location'):
            instance.location=validated_data.pop('location')
        if validated_data.get('middle_name'):
            instance.middle_name = validated_data.pop('middle_name')
        if validated_data.get('email'):
            instance.email = validated_data.pop('email')
        instance.save()
        return instance
        # validated_data['is_staff'] = False
        # buyr = Buyer.objects.create(**validated_data)
        # try:
        #     buyr.set_password(pwd)
        #     buyr.save()
        #
        # except Exception as e:
        #     buyr.delete()
        # return buyr

class UserUpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username=serializers.ReadOnlyField()
    password = serializers.ReadOnlyField()
    is_staff=serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id','username','email','is_staff']
        extra_kwargs = {"password": {"write_only": True}}



class SellerSerializer(UserSerializer):
    id = serializers.ReadOnlyField()
    description = serializers.CharField(max_length=1000, allow_null=True,default=None)
    location = serializers.CharField(allow_blank=True,allow_null=True,default=None)
    middle_name = serializers.CharField(allow_null=True,default=None)
    phone_number = serializers.IntegerField(allow_null=True,default=None)
    profile_pic=serializers.ImageField(allow_null=True,default=None)
    first_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False, allow_null=False)
    email = serializers.EmailField()

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
        return sllr
    def update(self, instance,validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        pwd = validated_data.pop('password')
        if validated_data.get('location'):
            instance.location=validated_data.pop('location')
        if validated_data.get('middle_name'):
            instance.middle_name = validated_data.pop('middle_name')
        if validated_data.get('description'):
            instance.description = validated_data.pop('description')
        if validated_data.get('phone_number'):
            instance.phone_number = validated_data.pop('phone_number')
        instance.save()
        return instance


class SellerUpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    description = serializers.CharField(max_length=1000, allow_null=True)
    location = serializers.CharField(allow_blank=True,allow_null=True)
    middle_name = serializers.CharField(allow_null=True,default=None)
    phone_number = serializers.IntegerField(allow_null=True)
    first_name = serializers.CharField(max_length=50, min_length=2, allow_null=True)
    last_name = serializers.CharField(max_length=50, min_length=2,allow_null=True)
    profile_pic=serializers.ImageField(allow_null=True,default=None)
    email = serializers.EmailField()
    is_staff=serializers.ReadOnlyField()
    username=serializers.ReadOnlyField()


    class Meta:
        model = Seller
        fields = '__all__'

    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        pwd = validated_data.pop('password')
        validated_data['is_staff'] = True
        sllr = Seller.objects.create(**validated_data)
        return sllr
    def update(self, instance,validated_data):


        # if validated_data.get('location'):
        #     instance.location=validated_data.pop('location')
        # if validated_data.get('middle_name'):
        #     instance.middle_name = validated_data.pop('middle_name')
        # if validated_data.get('description'):
        #     instance.description = validated_data.pop('description')
        # if validated_data.get('phone_number'):
        #     instance.phone_number = validated_data.pop('phone_number')
        # if validated_data.get('first_name'):
        #     instance.first_name = validated_data.pop('first_name')
        # if validated_data.get('last_name'):
        #     instance.last_name = validated_data.pop('last_name')
        image=validated_data.pop('profile_pic')
        print(validated_data)
        if image:
            if image == '':
                image = None
            instance = Seller.objects.get(pk=instance.id)
            instance.profile_pic = image
            instance.save()

        Seller.objects.filter(pk=instance.id).update(**validated_data)
        user = Seller.objects.get(pk=instance.id)
        return user

class BuyerUpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    location = serializers.CharField(allow_blank=False,allow_null=True,default=None)
    middle_name = serializers.CharField(allow_null=True,default=None)
    first_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=50, min_length=2, allow_blank=False, allow_null=False)
    profile_pic=serializers.ImageField(allow_null=True,default=None)
    email = serializers.EmailField()
    is_staff=serializers.ReadOnlyField()
    username=serializers.ReadOnlyField()

    class Meta:
        model = Buyer
        fields = '__all__'
    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        pwd = validated_data.pop('password')
        validated_data['is_staff'] = False
        buyr = Buyer.objects.create(**validated_data)
        return buyr

    def update(self, instance,validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        # buyer = Buyer.objects.get(pk=instance.id)
        # if validated_data.get('location'):
        #     instance.location=validated_data.pop('location')
        # if validated_data.get('middle_name'):
        #     instance.middle_name = validated_data.pop('middle_name')
        # if validated_data.get('email'):
        #     instance.email = validated_data.pop('email')
        # if validated_data.get('first_name'):
        #     instance.first_name = validated_data.pop('first_name')
        # if validated_data.get('last_name'):
        #     instance.last_name = validated_data.pop('last_name')
        # if validated_data.get('profile_pic'):
        #     instance.profile_pic = validated_data.pop('profile_pic')
        # instance.save()
        image=validated_data.pop('profile_pic')

        if image:
            if image=='':
                image=None
            instance = Buyer.objects.get(pk=instance.id)
            instance.profile_pic = image
            instance.save()

        Buyer.objects.filter(pk=instance.id).update(**validated_data)
        user = Buyer.objects.get(pk=instance.id)
        return user