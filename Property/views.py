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
from .serializer import PropertySerializer,PropertyImageSerializer
from .models import Property,PropertyImages
from rest_framework.mixins import UpdateModelMixin
from django.db import transaction

class PropertyView(generics.ListCreateAPIView,UpdateModelMixin):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        images=[]
        if serializer.is_valid():
            serializer.save()
            for upfile in request.FILES.getlist('images'):
                pf=PropertyImageSerializer(data={'file':upfile,'property':serializer.data['id']})
                if pf.is_valid():
                    pf.save()
                    images.append(pf.data)
                    print(pf.data)
                else:
                    print(pf.errors)
        else:
            print(serializer.errors)
            return Response(status=404)
        return Response({'property':serializer.data,'images':images},status=status.HTTP_200_OK)
    # def get(self,request):
    #     propObj=Property.objects.all()
    #     seri=PropertySerializer(propObj,many=True)
    #     return Response(seri.data, status=status.HTTP_200_OK)

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









