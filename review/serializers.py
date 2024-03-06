from rest_framework import serializers
from .models import Review
from rating.serializers import RatingSerializer
from rating.models import Rating


class ReviewSerializer(serializers.ModelSerializer):
    rating = RatingSerializer()

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        rating_data = validated_data.pop('rating')
        rating = Rating.objects.create(**rating_data)
        rating.save()

        review = Review.objects.create(**validated_data)
        review.rating = rating
        review.save()

        return review

    def update(self, instance, validated_data):
        if "rating" in validated_data:
            rating_data = validated_data.pop('rating')
            rating_instance = instance.rating
            for attr, value in rating_data.items():
                setattr(rating_instance, attr, value)
                rating_instance.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
