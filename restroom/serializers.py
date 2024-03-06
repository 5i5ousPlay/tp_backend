from rest_framework import serializers
from .models import Restroom
from django.db.models import Avg
from review.serializers import ReviewSerializer
from tag.serializers import TagSerializer


class RestroomSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(method_name='get_rating')

    class Meta:
        model = Restroom
        fields = '__all__'

    def get_rating(self, obj):
        rating = obj.ratings.aggregate(Avg("rating", default=0))
        return rating['rating__avg']


class RestroomGETSerializer(RestroomSerializer):
    reviews = ReviewSerializer(many=True)
    tags = TagSerializer(many=True)
