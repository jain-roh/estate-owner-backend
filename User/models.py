from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Seller(User):

    description=models.CharField(max_length=1000,null=False)
    location=models.CharField(max_length=200,blank=True)
    middle_name=models.CharField(max_length=200,null=True)
    phone_number=models.BigIntegerField()

class Buyer(User):

    location = models.CharField(max_length=200,blank=False)
    middle_name = models.CharField(max_length=200,null=True)
