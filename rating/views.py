from django.shortcuts import render
from .models import Rating
from .serializers import RatingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


class RatingListView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingDetailView(generics.RetrieveUpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser]


class RatingDeleteView(generics.DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'pk'
