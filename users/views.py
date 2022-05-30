from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import RegisterSerializer
# Create your views here.


class UserApi(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer
