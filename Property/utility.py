import datetime
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
from .serializer import PropertySerializer
from rest_framework import status
from rest_framework.response import Response

def create_property(request):
    print(request.data)
    serializer = PropertySerializer(data=request.data)
    # file_obj = request.FILES['file']
    if serializer.is_valid():
        serializer.save()

        # UserRegister.objects.create_user(username==serializer.data)
        # User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'],email=serializer.data['email'],is_staff=serializer.data['is_staff'])
        return Response(serializer.data,status= status.HTTP_200_OK)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






