from rest_framework.views import APIView
from rest_framework import generics
class HealthCheck(generics.ListAPIView):

    def get(self,request):
        return Response({},status=status.HTTP_200_OK)