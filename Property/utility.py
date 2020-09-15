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

def search_property(request):
    property_list = Property.objects.all()
    property_filter = PropertyFilter(request.GET, queryset=property_list)
    print(property_filter.qs)
    ids=property_filter.qs.values_list('id', flat=True)
    print(ids)
    serializer=PropertySerializer(property_filter.qs,many=True)
    image_list=PropertyImages.objects.filter(id__in=ids)
    imageSeriazlizer=PropertyImageSerializer(image_list,many=True)
    return Response({'property':serializer.data,'images':imageSeriazlizer.data}, status=status.HTTP_200_OK)





