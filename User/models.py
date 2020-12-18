from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from EstateByTheOwner.storage_backends import PublicMediaStorage,PrivateMediaStorage,ThumbnailStorage,PrivateMediaProfileStorage
from EstateByTheOwner.model_utility import make_thumbnail

class Seller(User):
    profile_pic = models.ImageField(storage=PrivateMediaProfileStorage(),null=True, default=None)
    description=models.CharField(max_length=1000,null=True,default=None)
    location=models.CharField(max_length=200,blank=True,null=True,default=None)
    middle_name=models.CharField(max_length=200,null=True,default=None)
    phone_number=models.BigIntegerField(null=True,default=None)
    def save(self, *args, **kwargs):
        if self.profile_pic:
            self.profile_pic = make_thumbnail(self.profile_pic, size=(350, 300))

        super().save(*args, **kwargs)
class Buyer(User):
    profile_pic = models.ImageField(storage=PrivateMediaProfileStorage(),null=True, default=None)
    location = models.CharField(max_length=200,blank=False,null=True,default=None)
    middle_name = models.CharField(max_length=200,null=True,default=None)

    def save(self, *args, **kwargs):
        if self.profile_pic:
            self.profile_pic = make_thumbnail(self.profile_pic, size=(350, 300))
