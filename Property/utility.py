import datetime
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
from .serializer import PropertySerializer
from rest_framework import status
from rest_framework.response import Response
from .filters import PropertyFilter
from .models import Property

def search_property(request):
    property_list = Property.objects.all()
    property_filter = PropertyFilter(request.GET, queryset=property_list)
    print(property_filter.qs)
    serializer=PropertySerializer(property_filter.qs,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)





