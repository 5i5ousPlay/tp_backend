from rest_framework import serializers
from .models import Building
from restroom.serializers import RestroomSerializer


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = "__all__"


class BuildingGETSerializer(BuildingSerializer):
    restrooms = RestroomSerializer(many=True)