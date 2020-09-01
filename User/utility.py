from jose import jws
from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
from .serializer import BuyerSerializer,SellerSerializer
from .models import Buyer,Seller
from django.core import serializers

def create_jwt(request):
    """
    the above token need to be saved in database, and a one-to-one
    relation should exist with the username/user_pk
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    username = request.POST['username']
    password = request.POST['password']
    is_staff=request.POST['is_staff']
    user = authenticate(username=username, password=password,is_staff=is_staff)

    if user is None:
        return HttpResponse({'error':'Wrong Username or Password'}, status=400)
    if user.is_staff:
        user=Seller.objects.get(id=user.id)
    else:
        user=Buyer.objects.get(id=user.id)
    data=serializers.serialize('json',[user,])
    print(data)
    return None


def create_user(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    is_staff=request.POST['is_staff']
    if is_staff is None:
        return HttpResponse({'error':'Please verify weather user is Buyer or Seller'},statusx=400)

    if not is_staff:
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data=serializer.data
            data=data.pop('password',None)
            return tokenize(data,ip)
        return HttpResponse(serializer.errors, status=400)
    elif is_staff:
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data=serializer.data
            data.pop('password',None)
            return tokenize(data,ip)
        return HttpResponse(serializer.errors, status=400)



def tokenize(data,ip):
    expiry = datetime.date.today() + datetime.timedelta(days=30)
    expiry = json.dumps(
        expiry,
        sort_keys=True,
        indent=1,
        cls=DjangoJSONEncoder
    )

    if data is None:
        return HttpResponse([{'error': 'Error Logging in an user'}], status=400)
    data.expiry=expiry
    token = jws.sign(data,
                     'seKre8' + ip, algorithm='HS256')
    return HttpResponse(token,status=201)




