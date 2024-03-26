from rest_framework import serializers
from .models import CustomUser as User
from review.serializers import ReviewSerializer
from core.utils.serializers import UserSerializer


class UserProfileSerializer(UserSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'reviews', 'is_staff']
