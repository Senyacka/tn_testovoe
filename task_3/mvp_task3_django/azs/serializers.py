from rest_framework import serializers
from azs.models import (AZS,
                        Service,
                        AZSService,
                        Image,
                        AZSImage,
                        )


class AZSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AZS
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class AZSServiceSerializer(serializers.ModelSerializer):
    service_id = serializers.SerializerMethodField(allow_null=True)
    service_description = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = AZSService
        fields = ["azs", "service_id", "service_description", "status"]

    def get_service_id(self, instance):
        return instance.service.id

    def get_service_description(self, instance):
        return instance.service.description


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class AZSImageSerializer(serializers.ModelSerializer):
    image_id = serializers.SerializerMethodField(allow_null=True)
    image_url = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = AZSImage
        fields = ["azs", "image_id", "image_url"]

    def get_image_id(self, instance):
        return instance.image.id

    def get_image_url(self, instance):
        return instance.image.url
