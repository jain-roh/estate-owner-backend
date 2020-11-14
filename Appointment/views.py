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

class AppointViewAll(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    def get(self,request,*args, **kwargs):
        print(kwargs,args,request.GET)
        if request.GET.get('buyer',None):
            appointment_obj=Appointment.objects.filter(buyer=request.GET['buyer'])
        elif request.GET.get('seller',None):
            appointment_obj = Appointment.objects.filter(seller=request.GET['seller'])
        serializer = AppointmentSerializer(appointment_obj,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)











