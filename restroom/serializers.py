from rest_framework import serializers
from .models import Restroom


class RestroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restroom
        fields = '__all__'
