from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserSerializer


# Create your views here.
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
