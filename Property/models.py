from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from User.models import Seller
from django.core.files.storage import FileSystemStorage
from EstateByTheOwner.storage_backends import PublicMediaStorage,PrivateMediaStorage,ThumbnailStorage
from .model_utility import make_thumbnail


class Property(models.Model):
   user=models.ForeignKey(Seller,related_name='user_id',on_delete=models.CASCADE)
   address1 = models.CharField(db_index=True,max_length=200,null=False,default='')
   address2 = models.CharField(max_length=200, null=True)
   city = models.CharField(max_length=200, null=False,default='')
   state = models.CharField(max_length=200, null=False,default='')
   zipcode = models.CharField(max_length=10, null=False,default='')
   latitude=models.FloatField(null=False)
   longitude = models.FloatField(null=False)
   price=models.FloatField(db_index=True,validators=[MinValueValidator(1,00)],default=1.00)
   beds=models.FloatField(db_index=True,validators=[MinValueValidator(0,00)],default=1.00)
   bath=models.FloatField(db_index=True,validators=[MinValueValidator(0,99)],default=1.00)
   size = models.FloatField(validators=[MinValueValidator(10,00)], default=1.00)
   description = models.CharField(max_length=1000, null=True)
   image_ico = models.ImageField(storage=PrivateMediaStorage(),null=True, default=None)
   video=models.FileField(storage=PrivateMediaStorage(),null=True,default=None)
   CHOICES = [('townhouse', 'Townhouse'),
              ('condo', 'Condo'),
              ('apartment', 'Apartment'),
              ('commercial', 'Commercial')
              ]
   propertytype = models.CharField(db_index=True,
      choices=CHOICES,
      default='townhouse', max_length=50)

   def save(self, *args, **kwargs):
      if self.image_ico:
         self.image_ico = make_thumbnail(self.image_ico, size=(350, 300))
      super().save(*args, **kwargs)
   class Meta:
      db_table = "property"



class PropertyImages(models.Model):
   property=models.ForeignKey(Property,related_name='property_image')
   file=models.ImageField(storage=PrivateMediaStorage())
   class Meta:
      db_table='property_img'