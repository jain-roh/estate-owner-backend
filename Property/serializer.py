from rest_framework import serializers
import re
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Property,PropertyImages
from User.models import Seller

class PropertyImageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    property=serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())
    file=serializers.ImageField()
    display=serializers.BooleanField(default=True,allow_null=True)
    class Meta:
        model = PropertyImages
        fields = '__all__'
    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        return PropertyImages.objects.create(**validated_data)

class PropertyImageUpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    display=serializers.BooleanField(default=True)
    class Meta:
        model = PropertyImages
        fields = '__all__'
    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        return PropertyImages.objects.create(**validated_data)
    def update(self,instance,validated_data):
        prop = PropertyImages.objects.get(pk=instance.id)
        PropertyImages.objects.filter(pk=instance.id) \
            .update(**validated_data)
        # print(validated_data)
        # instance.property_image=validated_data.get('property_image')
        # instance.save()

        return prop

class PropertySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user=serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    address1 = serializers.CharField(max_length=200, allow_null=False)
    address2 = serializers.CharField(max_length=200, allow_null=True)
    city = serializers.CharField(max_length=200, allow_null=False)
    state = serializers.CharField(max_length=200, allow_null=False)
    zipcode = serializers.CharField(max_length=10, allow_null=False)
    latitude = serializers.FloatField(allow_null=False)
    longitude = serializers.FloatField(allow_null=False)
    price = serializers.FloatField(validators=[MinValueValidator(1, 00)], default=1.00)
    beds = serializers.FloatField(validators=[MinValueValidator(0, 00)], default=1.00)
    bath = serializers.FloatField(validators=[MinValueValidator(0, 99)], default=1.00)
    size = serializers.FloatField(validators=[MinValueValidator(10, 00)], default=1.00)
    description = serializers.CharField(max_length=1000, allow_null=True)
    image_ico=serializers.ImageField(allow_null=True,default=None)
    video=serializers.FileField(allow_null=True,default=None)
    CHOICES = [('townhouse', 'Townhouse'),
               ('condo', 'Condo'),
               ('apartment', 'Apartment'),
               ('commercial', 'Commercial')
               ]
    propertytype = serializers.ChoiceField(
        choices=CHOICES,
        default='townhouse')
    property_image = PropertyImageSerializer(many=True,read_only=True,allow_null=True)
    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        return Property.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # prop = Property.objects.get(pk=instance.id)
        # print(validated_data.get('video'))
        #
        if validated_data.get('video',None):
            instance.video=validated_data.pop('video')
            instance.save()


        Property.objects.filter(pk=instance.id) \
            .update(**validated_data)
        prop = Property.objects.get(pk=instance.id)
        return prop

class PropertyUpdateSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user=serializers.ReadOnlyField()
    address1 = serializers.CharField(max_length=200, allow_null=False)
    address2 = serializers.CharField(max_length=200, allow_null=True)
    city = serializers.CharField(max_length=200, allow_null=False)
    state = serializers.CharField(max_length=200, allow_null=False)
    zipcode = serializers.CharField(max_length=10, allow_null=False)
    latitude = serializers.FloatField(allow_null=False)
    longitude = serializers.FloatField(allow_null=False)
    price = serializers.FloatField(validators=[MinValueValidator(1, 00)], default=1.00)
    beds = serializers.FloatField(validators=[MinValueValidator(0, 00)], default=1.00)
    bath = serializers.FloatField(validators=[MinValueValidator(0, 99)], default=1.00)
    size = serializers.FloatField(validators=[MinValueValidator(10, 00)], default=1.00)
    description = serializers.CharField(max_length=1000, allow_null=True)
    image_ico=serializers.ImageField(allow_null=True,default=None)
    video=serializers.FileField(allow_null=True,default=None)
    CHOICES = [('townhouse', 'Townhouse'),
               ('condo', 'Condo'),
               ('apartment', 'Apartment'),
               ('commercial', 'Commercial')
               ]
    propertytype = serializers.ChoiceField(
        choices=CHOICES,
        default='townhouse')
    property_image = PropertyImageSerializer(many=True,read_only=True,allow_null=True)
    class Meta:
        model = Property
        fields = '__all__'

    def create(self, validated_data):
        return Property.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # prop = Property.objects.get(pk=instance.id)
        # print(validated_data.get('video'))
        #
        if validated_data.get('video',None):
            instance.video=validated_data.pop('video')
            instance.save()


        Property.objects.filter(pk=instance.id) \
            .update(**validated_data)
        prop = Property.objects.get(pk=instance.id)
        return prop