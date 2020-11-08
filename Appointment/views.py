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
from .serializer import AppointmentSerializer
from .models import Appointment
from rest_framework.mixins import UpdateModelMixin

class AppointmentView(generics.ListCreateAPIView,UpdateModelMixin):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


    def post(self, request):
        print(request.data)
        return self.create(request)

    def put(self,request,*args, **kwargs):
        return self.partial_update(request, *args, **kwargs)











