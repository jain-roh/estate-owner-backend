from rest_framework import generics
from .utility import create_jwt,create_user


class UserLogin(generics.ListCreateAPIView):

    def post(self, request):
        return create_jwt(request)

class CreateUser(generics.ListCreateAPIView):

    def post(self, request):
        return create_user(request)







