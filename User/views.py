from rest_framework import generics
from .utility import create_jwt,create_user,update_user,fetch_user,change_password
from .serializer import UserSerializer,SellerSerializer
from .models import User,Seller
from rest_framework.response import Response
from rest_framework import status
import json
class UserLogin(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        data=request.POST
        if data.get('data',None):
            import requests
            data=json.loads(data.get('data'))
            print(data)
            response=requests.get('https://graph.facebook.com/'+str(data.get('userID')+'?fields=name,first_name,last_name,email,id&access_token='+str(data.get('accessToken'))))
            temp_data={}
            temp_data['first_name']=response.data['first_name']
            print(temp_data)
            temp_data['last_name'] = response.data['last_name']
            temp_data['username'] = response.data['id']
            temp_data['email'] = response.data['email']
            temp_data['is_staff']=False
            temp_data['password']='Test'
            print(temp_data)
            serializer = BuyerSerializer(data=temp_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                data=serializer.data
                data.pop('password',None)
                print(data)
                return tokenize(data,ip)
            print(serializer.errors)
            return HttpResponse(serializer.errors, status=400)
        else:
            return create_jwt(request)

class UserUpdate(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        return change_password(request)

class CreateUser(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        return create_user(request)
    def put(self,request,*args, **kwargs):
        if not request.user2:
            return Response({'Invalid Token'}, status=400)
        return update_user(request)
    def get(self,request):
        if not request.user2:
            return Response({'Invalid Token'}, status=400)

        return fetch_user(request)



class SellerDetails(generics.ListCreateAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    def get(self, request):
        user_obj = Seller.objects.get(pk=request.GET['seller'])
        user_serializer = SellerSerializer(user_obj)
        return Response(user_serializer.data, status=status.HTTP_200_OK)








