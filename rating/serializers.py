from rest_framework import serializers
from .models import Rating
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0)
    ])

    class Meta:
        model = Rating
        fields = '__all__'


class ReviewRatingSerializer(RatingSerializer):
    restroom = serializers.CharField(required=False)
