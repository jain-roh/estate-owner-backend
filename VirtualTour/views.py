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
from .serializer import VirtualTourSerializer
from .models import VirtualTour
from rest_framework.mixins import UpdateModelMixin

class VirtualTourView(generics.ListCreateAPIView,UpdateModelMixin):
    serializer_class = VirtualTourSerializer
    queryset = VirtualTour.objects.all()


    def post(self, request):
        return self.create(request)













