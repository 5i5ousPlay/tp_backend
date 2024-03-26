from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer, ReviewGETSerializer
from .permissions import IsReviewAuthor, IsReviewAuthorOrIsAdmin


# Create your views here.
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewGETSerializer
    permission_classes = [AllowAny]


class ReviewDetailView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated(), IsReviewAuthorOrIsAdmin()]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewGETSerializer
        else:
            return ReviewSerializer


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated & (IsReviewAuthor | IsAdminUser)]
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        try:
            rating = instance.rating
            rating.delete()
        except Exception as e:
            return Response({"detail": str(e.args[0])}, status=status.HTTP_400_BAD_REQUEST)
