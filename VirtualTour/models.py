from django.db import models
from User.models import Buyer,Seller
from Property.models import Property
from django.core.validators import MaxValueValidator, MinValueValidator

class VirtualTour(models.Model):
   buyer=models.ForeignKey(Buyer,related_name='buyer_id',on_delete=models.CASCADE)
   seller=models.ForeignKey(Seller,related_name='seller_id',on_delete=models.CASCADE)
   property=models.ForeignKey(Property,related_name='property_id',on_delete=models.CASCADE)
   datetime=models.DateTimeField()
   class Meta:
      db_table = "virtualtour"
