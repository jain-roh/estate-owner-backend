from rest_framework import generics
from .utility import create_jwt,create_user
from .serializer import UserSerializer,SellerSerializer
from .models import User,Seller
from rest_framework.response import Response
from rest_framework import status

class UserLogin(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        return create_jwt(request)


class CreateUser(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        print('I am here')
        return create_user(request)

class SellerDetails(generics.ListCreateAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    def get(self, request):
        user_obj = Seller.objects.get(pk=request.GET['seller'])
        user_serializer = SellerSerializer(user_obj)
        return Response(user_serializer.data, status=status.HTTP_200_OK)








