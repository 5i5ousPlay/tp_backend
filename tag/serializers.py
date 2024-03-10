from rest_framework import serializers
from .models import Tag
from django.conf import settings


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data['name']
        if name in settings.DEFAULT_TAGS:
            raise serializers.ValidationError(
                {"detail": "The name provided is a default tag. Please specify a different name."}
            )

        return super().create(validated_data)
