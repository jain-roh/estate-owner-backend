from rest_framework import generics
from .utility import create_jwt,create_user
from .serializer import UserSerializer
from .models import User
class UserLogin(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        return create_jwt(request)

class CreateUser(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def post(self, request):
        return create_user(request)







