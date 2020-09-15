from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from User.models import Seller
from django.core.files.storage import FileSystemStorage
from EstateByTheOwner.storage_backends import PublicMediaStorage,PrivateMediaStorage



class Property(models.Model):
   user=models.ForeignKey(Seller,related_name='user_id',on_delete=models.CASCADE)
   address1 = models.CharField(max_length=200,null=False,default='')
   address2 = models.CharField(max_length=200, null=True)
   city = models.CharField(max_length=200, null=False,default='')
   state = models.CharField(max_length=200, null=False,default='')
   zipcode = models.CharField(max_length=10, null=False,default='')
   latitude=models.FloatField(null=False)
   longitude = models.FloatField(null=False)
   price=models.FloatField(validators=[MinValueValidator(1,00)],default=1.00)
   beds=models.FloatField(validators=[MinValueValidator(0,00)],default=1.00)
   bath=models.FloatField(validators=[MinValueValidator(0,99)],default=1.00)
   size = models.FloatField(validators=[MinValueValidator(10,00)], default=1.00)
   description = models.CharField(max_length=1000, null=True)
   CHOICES = [('townhouse', 'Townhouse'),
              ('condo', 'Condo'),
              ('apartment', 'Apartment'),
              ('commercial', 'Commercial')
              ]
   propertytype = models.CharField(
      choices=CHOICES,
      default='townhouse', max_length=2)

   class Meta:
      db_table = "property"

class PropertyImages(models.Model):
   property=models.ForeignKey(Property)
   file=models.FileField(storage=PrivateMediaStorage())
   class Meta:
      db_table='property_img'