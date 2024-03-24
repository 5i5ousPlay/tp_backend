from rest_framework import serializers
from .models import Restroom
from django.db.models import Avg
from review.serializers import ReviewSerializer
from tag.serializers import TagSerializer
from image.serializers import ImageSerializer
from image.models import Image


class RestroomSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(method_name='get_rating')
    images = ImageSerializer(many=True)

    class Meta:
        model = Restroom
        fields = '__all__'

    def get_rating(self, obj):
        rating = obj.ratings.aggregate(Avg("rating", default=0))
        return rating['rating__avg']

    def create(self, validated_data):
        images = validated_data.pop('images')
        restroom = super().create(validated_data)
        for image_data in images:
            Image.objects.create(image=image_data['image'], restroom=restroom)

        return restroom


class RestroomGETSerializer(RestroomSerializer):
    reviews = ReviewSerializer(many=True)
    tags = TagSerializer(many=True)
