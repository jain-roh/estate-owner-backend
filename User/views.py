from rest_framework import generics
from .utility import create_jwt,create_user,update_user,fetch_user,change_password,tokenize
from .serializer import UserSerializer,SellerSerializer,BuyerSerializer
from .models import User,Seller,Buyer
from rest_framework.response import Response
from django.contrib.auth import authenticate
import jwt
from rest_framework import status
import json
from google.oauth2 import id_token

class UserLogin(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        data=request.POST
        if data.get('data',None):

            if data.get('type')=='facebook':
                import requests
                data=json.loads(data.get('data'))
                response=requests.get('https://graph.facebook.com/'+str(data.get('userID')+'?fields=name,first_name,last_name,email,id&access_token='+str(data.get('accessToken'))))
                response=json.loads(response.text)
                temp_data={}
                temp_data['first_name']=response['first_name']
                temp_data['last_name'] = response['last_name']
                temp_data['username'] = response['id']
                temp_data['email'] = response['email']
                temp_data['is_staff']=False
                temp_data['password']='Test1234'
                print(temp_data)
            else:
                from google.auth.transport import requests

                data = json.loads(data.get('data'))
                print(data)
                try:
                    request = requests.Request()

                    response = id_token.verify_oauth2_token(data['code'],
                        request, '371591667819-k8q68a5eq9ghrgkrjb5hfj7sjulfetmb.apps.googleusercontent.com')

                    if response['iss'] != 'https://accounts.google.com':
                        raise ValueError('Wrong issuer.')

                    # public_key=requests.get('https://www.googleapis.com/oauth2/v3/certs').text
                    # response=jwt.decode(data.get('code'),public_key)
                except Exception as e:
                    print(e)
                print(response)
                temp_data = {}
                temp_data['first_name'] = response['given_name']
                temp_data['last_name'] = response['family_name']
                temp_data['username'] = response['sub']
                temp_data['email'] = response['email']
                temp_data['is_staff'] = False
                temp_data['password'] = 'Test1234'
                print(temp_data)
            try:
                user=authenticate(username=temp_data['username'], password='Test1234')
                if user is None:
                    serializer = BuyerSerializer(data=temp_data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        data=serializer.data
                        data.pop('password',None)
                        print(data)
                        return tokenize(data,'aaa')
                    print(serializer.errors)
                else:
                    user = Buyer.objects.get(id=user.id)
                    user = BuyerSerializer(user)
                    data = user.data
                    data.pop('password', None)
                    return tokenize(data, 'aaa')
                return HttpResponse(serializer.errors, status=400)
            except Exception as e:
                print(e)
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








