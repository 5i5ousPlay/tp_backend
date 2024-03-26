from rest_framework import serializers
from .models import CustomUser as User
from review.serializers import ReviewGETSerializer
from core.utils.serializers import UserSerializer


class UserProfileSerializer(UserSerializer):
    reviews = ReviewGETSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'reviews', 'is_staff']
