from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def _validate_request_user(self, validated_data):
        """
        Checks if request user is admin depending on
        the presence of certain fields in submitted
        form data.
        """
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            user = request.user
            if 'restroom' in validated_data and not user.is_staff:
                raise serializers.ValidationError({"Unauthorized": "Only admins can upload / change "
                                                                   "images of restrooms"})
            if 'building' in validated_data and not user.is_staff:
                raise serializers.ValidationError({"Unauthorized": "Only admins can upload / change "
                                                                   "images of buildings"})

    def validate(self, attrs):

        # only allow uploading to either a building or restroom or review exclusively
        # uploads to two different instances are disallowed and will rais a validation error
        err_msg = {"detail": "An image can only be associated with a restroom, "
                             "review, or building, not multiple objects."}
        if attrs.get('restroom') and (attrs.get('review') or attrs.get('building')):
            raise serializers.ValidationError(
                err_msg)
        if attrs.get('review') and (attrs.get('restroom') or attrs.get('building')):
            raise serializers.ValidationError(
                err_msg)
        if attrs.get('building') and (attrs.get('restroom') or attrs.get('review')):
            raise serializers.ValidationError(
                err_msg)

        self._validate_request_user(attrs)

        return attrs


class B64ImageSerializer(ImageSerializer):
    image = Base64ImageField()
