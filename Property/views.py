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
from .serializer import PropertySerializer,PropertyImageSerializer,PropertyImageUpdateSerializer,PropertyUpdateSerializer
from .models import Property,PropertyImages
from rest_framework.mixins import UpdateModelMixin
from django.db import transaction
import copy
import json
class PropertyView(generics.ListCreateAPIView,UpdateModelMixin):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    def post(self, request):
        try:
            if not request.user2:
                return Response({'Invalid Token'},status=400)
            # elif int(request.user2['id'])!=int(request.data['user']):
            #     return Response({'Invalid Token'}, status=400)
            request.data['user']=request.user2['id']
            file_list=request.FILES.getlist('images',[])
            serializer = PropertySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                images=upload_property_image(file_list,serializer.data['id'])
            else:
                return Response(serializer.errors,status=404)
            return Response({'property':serializer.data,'images':images},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=400)

    def get(self,request,*args, **kwargs):
        propObj=Property.objects.get(pk=kwargs['pk'])
        serializer=PropertySerializer(propObj)
        prop=PropertyImages.objects.filter(property=kwargs['pk'],display=True)
        serializer2=PropertySerializer(propImage,many=True)
        return Response({'property':serializer.data,'images':serializer2.data}, status=status.HTTP_200_OK)

    def put(self,request,*args, **kwargs):
        print(request.user2)
        print(request.data)
        if not request.user2:
            return Response({'Invalid Token'}, status=400)
        # elif int(request.user2['id']) != int(request.data['user']):
        #     return Response({'Invalid Token'}, status=400)
        # request.data['user'] = request.user2['id']

        _mutable = request.data._mutable
        request.data._mutable = True

        images=request.data.pop('images', [])
        property_image = request.data.pop('property_image', [])
        request.data._mutable = _mutable
        # request.data._mutable = False

        prop = Property.objects.get(id=int(request.data['id']),user=request.user2['id'])
        serializer = PropertyUpdateSerializer(prop,request.data)
        if serializer.is_valid():
            serializer.save()
            property_data=serializer.data
            images_res = upload_property_image(images, serializer.data['id'])
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=400)

        for prop_img in property_image:

            prop_img=json.loads(prop_img)
            prop_img_obj=PropertyImages.objects.get(id=prop_img.get('id'))
            print(prop_img['display'])
            prop_img_obj.display=prop_img['display']
            prop_img_obj.save()
            # prop_img_serializer=PropertyImageUpdateSerializer(data=prop_img_obj)
            # print(prop_img_serializer)

            # if prop_img_serializer.is_valid():
            # prop_img_serializer.display
            # prop_img_serializer.save()
            # else:
            #     print(prop_img_serializer.errors)
            #     return Response(prop_img_serializer.errors, status=400)
        return Response({'property': property_data, 'images': images_res}, status=200)
        # return self.partial_update(request, *args, **kwargs)
class PropertySearchView(generics.ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

    def get(self,request):
        return search_property(request)









