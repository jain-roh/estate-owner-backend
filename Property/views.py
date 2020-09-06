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
from .utility import search_property
from .serializer import PropertySerializer
from .models import Property
from rest_framework.mixins import UpdateModelMixin

class PropertyView(generics.ListCreateAPIView,UpdateModelMixin):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def post(self, request):
        return self.create(request)

    def put(self,request,*args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def get(self,request,*args, **kwargs):
        propObj=Property.objects.get(pk=kwargs['pk'])
        seri=PropertySerializer(propObj)
        return Response(seri.data, status=status.HTTP_200_OK)


class PropertySearchView(generics.ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def get(self,request):
        return search_property(request)









