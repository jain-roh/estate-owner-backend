from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.response import Response
from django.views import generic
from django.contrib.auth.models import User
from .utility import create_property
from .serializer import PropertySerializer
from .models import Property

class PropertyView(generics.ListCreateAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def post(self, request):
        return create_property(request)







