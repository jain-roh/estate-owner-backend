import datetime
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
from .serializer import PropertySerializer, PropertyImageSerializer
from rest_framework import status
from rest_framework.response import Response
from .filters import PropertyFilter
from .models import Property, PropertyImages
import uuid

def search_property(request):
    property_list = Property.objects.all()
    print(request.data)
    property_filter = PropertyFilter(request.data, queryset=property_list)
    print(property_filter.qs)
    ids=property_filter.qs.values_list('id', flat=True)
    serializer=PropertySerializer(property_filter.qs,many=True)
    # image_list=PropertyImages.objects.filter(id__in=ids)
    # imageSeriazlizer=PropertyImageSerializer(image_list,many=True)
    return Response({'property':serializer.data}, status=status.HTTP_200_OK)

def generate_file_name(file_name):
    name=file_name.rsplit('.',1)
    return name[0]+'_'+ str(uuid.uuid4())+'.'+name[1]

def upload_property_image(files,id):
    images=[]
    # if new_file:
    #     new_file.seek(0)
    for upfile in files:
        upfile.name=generate_file_name(upfile.name)
        pf = PropertyImageSerializer(data={'file': upfile, 'property': id})
        if pf.is_valid():
            pf.save()
            images.append(pf.data)
        else:
            images.append(pf.errors)
    return images






