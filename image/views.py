from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Image
from .serializers import ImageSerializer, B64ImageSerializer
from .permissions import IsImageOwner


# Create your views here.
class ImageUploadView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = B64ImageSerializer
    permission_classes = [IsAuthenticated]


class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]


class ImageDetailView(generics.RetrieveUpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = B64ImageSerializer
    permission_classes = [IsAuthenticated & (IsImageOwner | IsAdminUser)]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return super().get_permissions()


class ImageDeleteView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated & (IsImageOwner | IsAdminUser)]
