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
        file_list=request.FILES.getlist('images',[])
        # print(request.data)
        if len(file_list)>0:
            new_file=copy.deepcopy(file_list[0])
            new_file.name=generate_file_name(new_file.name)
            # temp=copy.deepcopy(new_file)

            request.data['image_ico']=new_file
            file_list[0].seek(0)

        request.data.copy()
        # request.data['video']=request.FILES.get('video',None)
        # request.data['video']=None
        serializer = PropertySerializer(data=request.data)
        images=[]
        if serializer.is_valid():
            serializer.save()
            images=upload_property_image(file_list,serializer.data['id'])
        else:
            return Response(serializer.errors,status=404)
        return Response({'property':serializer.data,'images':images},status=status.HTTP_200_OK)


    def get(self,request,*args, **kwargs):
        propObj=Property.objects.get(pk=kwargs['pk'])
        serializer=PropertySerializer(propObj)
        propImage=PropertyImages.objects.filter(property=kwargs['pk'])
        serializer2=PropertyImageSerializer(propImage,many=True)
        return Response({'property':serializer.data,'images':serializer2.data}, status=status.HTTP_200_OK)

class PropertySearchView(generics.ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def get(self,request):
        return search_property(request)









