from rest_framework import generics
from azs.models import (AZS,
                        AZSService,
                        Service,
                        Image,
                        AZSImage,
                        )
from azs.serializers import (AZSSerializer,
                             AZSServiceSerializer,
                             ServiceSerializer,
                             ImageSerializer,
                             AZSImageSerializer,
                             )


class AZSList(generics.ListAPIView):
    queryset = AZS.objects.all()
    serializer_class = AZSSerializer


class AZSDetail(generics.RetrieveAPIView):
    queryset = AZS.objects.all()
    serializer_class = AZSSerializer


class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AZSServiceList(generics.ListAPIView):
    queryset = AZSService.objects.all()
    serializer_class = AZSServiceSerializer


class AZSServiceDetail(generics.RetrieveAPIView):
    queryset = AZSService.objects.all()
    serializer_class = AZSServiceSerializer


class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class AZSImageList(generics.ListAPIView):
    queryset = AZSImage.objects.all()
    serializer_class = AZSImageSerializer


class AZSImageDetail(generics.RetrieveAPIView):
    queryset = AZSImage.objects.all()
    serializer_class = AZSImageSerializer
