from rest_framework import serializers

from images import models


class ImageSerializer(serializers.ModelSerializer):
    """ Serializar objeto de imagen """

    class Meta:
        model = models.Image
        fields = '__all__'


class DeleteImageSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255)
