from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Property(models.Model):
   user=models.ForeignKey(User,related_name='user_id')
   name = models.CharField(max_length=200,null=True)
   neighbourhood = models.CharField(max_length=200, null=True)
   latitude=models.FloatField()
   longitude = models.FloatField()
   price=models.FloatField(validators=[MinValueValidator(1,00)],default=1.00)
   beds=models.FloatField(validators=[MinValueValidator(0,00)],default=1.00)
   bath=models.FloatField(validators=[MinValueValidator(0,99)],default=1.00)
   size = models.FloatField(validators=[MinValueValidator(10,00)], default=1.00)
   description = models.CharField(max_length=1000, null=True)
   CHOICES = [('residential', 'Residential'),
              ('commercial', 'Commercial')]
   propertytype = models.CharField(
      choices=CHOICES,
      default='residential', max_length=2)
   class Meta:
      db_table = "property"
