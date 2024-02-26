from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Restroom
from .serializers import RestroomSerializer


# Create your views here.
class RestroomCreateView(generics.CreateAPIView):
    queryset = Restroom.objects.all()
    serializer_class = RestroomSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class RestroomListView(generics.ListAPIView):
    queryset = Restroom.objects.all()
    serializer_class = RestroomSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class RestroomDetailView(generics.RetrieveUpdateAPIView):
    queryset = Restroom.objects.all()
    serializer_class = RestroomSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'pk'


class RestroomDeleteView(generics.DestroyAPIView):
    queryset = Restroom.objects.all()
    serializer_class = RestroomSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'pk'
