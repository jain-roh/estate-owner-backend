from django.db import models
from User.models import Buyer,Seller
from Property.models import Property
from django.core.validators import MaxValueValidator, MinValueValidator

class Appointment(models.Model):
   buyer=models.ForeignKey(Buyer,related_name='buyer_id',on_delete=models.CASCADE)
   seller=models.ForeignKey(Seller,related_name='seller_id',on_delete=models.CASCADE)
   property=models.ForeignKey(Property,related_name='property_id',on_delete=models.CASCADE)
   datetime=models.DateTimeField()
   CHOICES = [('accept', 'Accept'),
              ('reschedule', 'Reschedule'),
              ('reject', 'Reject')]
   response = models.CharField(
      choices=CHOICES,
      default=None, max_length=2,null=True)
   reschedule = models.IntegerField(null=True)
   class Meta:
      db_table = "appointment"
