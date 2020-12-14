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
from .serializer import AppointmentSerializer,AppointmentViewSerializer
from .models import Appointment
from rest_framework.mixins import UpdateModelMixin
import json

class AppointmentView(generics.ListCreateAPIView,UpdateModelMixin):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


    def post(self, request):
        mutable = request.POST._mutable
        request.POST._mutable = True
        if bool(request.user2['is_staff']):
            request.data['seller']=request.user2['id']
        elif not bool(request.user2['is_staff']):
            request.data['buyer'] = request.user2['id']
        request.POST._mutable = mutable
        return self.create(request)

    def put(self,request,*args, **kwargs):
        # mutable = request.POST._mutable
        # request.POST._mutable = True
        # if bool(request.user2['is_staff']):
        #     request.data['seller']=request.user2['id']
        # elif not bool(request.user2['is_staff']):
        #     request.data['buyer'] = request.user2['id']
        # request.POST._mutable = mutable
        print(kwargs,args)
        return self.partial_update(request, *args, **kwargs)

class AppointViewAll(generics.ListCreateAPIView):
    serializer_class = AppointmentViewSerializer
    queryset = Appointment.objects.all()
    def get(self,request,*args, **kwargs):
        id=None
        if bool(request.user2['is_staff']):
            id=request.user2['id']
        elif not bool(request.user2['is_staff']):
            id = request.user2['id']
        appointment_obj=None
        print(id)
        if not bool(request.user2['is_staff']):
            appointment_obj=Appointment.objects.filter(buyer=id)
        elif bool(request.user2['is_staff']):
            appointment_obj = Appointment.objects.filter(seller=id)
        serializer = AppointmentViewSerializer(appointment_obj,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)











