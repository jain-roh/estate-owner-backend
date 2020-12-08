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
from django.conf import settings

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
        user=SellerSerializer(user)
    else:
        user=Buyer.objects.get(id=user.id)
        user=BuyerSerializer(user)
    data = user.data
    data.pop('password', None)
    return tokenize(data, ip)
    # return HttpResponse(user.errors, status=400)


def create_user(request):
    print('I am here 2')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    is_staff=request.POST['is_staff']
    if is_staff is None:
        return HttpResponse({'error':'Please verify weather user is Buyer or Seller'},statusx=400)
    print(is_staff)
    if is_staff=='False':
        print('dd')
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data=serializer.data
            data.pop('password',None)
            return tokenize(data,ip)
        return HttpResponse(serializer.errors, status=400)
    elif is_staff=='True':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data=serializer.data
            data.pop('password',None)
            return tokenize(data,ip)
        print(serializer.errors)
        return HttpResponse(serializer.errors, status=400)



def tokenize(data,ip):
    try:
        expiry = datetime.date.today() + datetime.timedelta(minutes=2)
        expiry = json.dumps(
            expiry,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )
        hmac_key = {
            "kty": "oct",
            "kid": "018c0ae5-4d9b-471b-bfd6-eef314bc7037",
            "use": "sig",
            "alg": "HS256",
            "k": "hJtXIZ2uSN5kbQfbtTNWbpdmhkV8FJG-Onbc6mxCcYg"
        }
        if data is None:
            return HttpResponse([{'error': 'Error Logging in an user'}], status=400)
        data.expiry=expiry
        token = jws.sign(data,settings.PRIVATE_KEY, algorithm='RS256', headers={'kid':'HtUDDTau8PSYOLLSdKFvb86SNfJoTqiD8eeCNnva'})
        return HttpResponse([{'token':token}],status=201)
    except Exception as e:
        print(e)

def verify_token(token):
    try:
        data=jws.verify(token,settings.PRIVATE_KEY, algorithms=['RS256'])
        return json.loads(data)
    except Exception as e:
        pass





