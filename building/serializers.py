from rest_framework import serializers
from .models import Building
from restroom.serializers import RestroomSerializer
from image.serializers import ImageSerializer


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = "__all__"


class BuildingGETSerializer(BuildingSerializer):
    restrooms = RestroomSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)