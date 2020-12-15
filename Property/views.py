from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import status
from django.views import generic
from django.contrib.auth.models import User
from .utility import search_property,upload_property_image,generate_file_name
from .serializer import PropertySerializer,PropertyImageSerializer
from .models import Property,PropertyImages
from rest_framework.mixins import UpdateModelMixin
from django.db import transaction
import copy

class PropertyView(generics.ListCreateAPIView,UpdateModelMixin):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    def post(self, request):
        if not request.user2:
            return Response({'Invalid Token'},status=400)
        elif request.user2['id']!=request.data['user']:
            return Response({'Invalid Token'}, status=400)
        file_list=request.FILES.getlist('images',[])
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            images=upload_property_image(file_list,serializer.data['id'])
        else:
            return Response(serializer.errors,status=404)
        return Response({'property':serializer.data,'images':images},status=status.HTTP_200_OK)


    def get(self,request,*args, **kwargs):
        propObj=Property.objects.get(pk=kwargs['pk'])
        serializer=PropertySerializer(propObj)
        propImage=PropertyImages.objects.filter(property=kwargs['pk'],display=True)
        serializer2=PropertyImageSerializer(propImage,many=True)
        return Response({'property':serializer.data,'images':serializer2.data}, status=status.HTTP_200_OK)

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
class PropertySearchView(generics.ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def get(self,request):
        return search_property(request)









