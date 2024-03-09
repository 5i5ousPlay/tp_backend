from rest_framework import serializers
from django.db import transaction
from .models import Review
from rating.serializers import RatingSerializer
from rating.models import Rating
from image.serializers import ImageSerializer, B64ImageSerializer
from image.models import Image


class ReviewSerializer(serializers.ModelSerializer):
    rating = RatingSerializer()
    images = B64ImageSerializer(many=True)

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        try:
            with transaction.atomic():
                rating_data = validated_data.pop('rating')
                images = validated_data.pop('images')

                rating = Rating.objects.create(**rating_data)
                rating.save()

                review = Review.objects.create(**validated_data)
                review.rating = rating
                review.save()

                for image_data in images:
                    Image.objects.create(review=review, uploaded_by=review.author, **image_data)

        except Exception as e:
            raise ValueError(str(e))

        return review

    def update(self, instance, validated_data):
        try:
            with transaction.atomic():
                if "rating" in validated_data:
                    rating_data = validated_data.pop('rating')
                    rating_instance = instance.rating
                    for attr, value in rating_data.items():
                        setattr(rating_instance, attr, value)
                        rating_instance.save()
                for attr, value in validated_data.items():
                    setattr(instance, attr, value)
                instance.save()
        except Exception as e:
            raise ValueError(str(e))
        return instance
