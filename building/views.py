from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Building
from .serializers import BuildingSerializer, BuildingGETSerializer


# Create your views here.
class BuildingCreateView(generics.CreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class BuildingListView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingGETSerializer


class BuildingDetailView(generics.RetrieveUpdateAPIView):
    queryset = Building.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated(), IsAdminUser()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BuildingGETSerializer
        else:
            return BuildingSerializer


class BuildingDeleteView(generics.DestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'pk'
