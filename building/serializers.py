from rest_framework import serializers
from .models import Building
from restroom.serializers import RestroomSerializer


class BuildingSerializer(serializers.ModelSerializer):
    restrooms = RestroomSerializer(many=True)

    class Meta:
        model = Building
        fields = ['id', 'name', 'description', 'restrooms']
