from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Seller(User):

    description=models.CharField(max_length=1000,null=True,default=None)
    location=models.CharField(max_length=200,blank=True,null=True,default=None)
    middle_name=models.CharField(max_length=200,null=True,default=None)
    phone_number=models.BigIntegerField(null=True,default=None)

class Buyer(User):

    location = models.CharField(max_length=200,blank=False,null=True,default=None)
    middle_name = models.CharField(max_length=200,null=True,default=None)
