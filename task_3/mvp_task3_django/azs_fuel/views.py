from rest_framework import generics
from azs_fuel.models import Fuel, AZSFuel
from azs_fuel.serializers import FuelSerializer, AZSFuelSerializer


class FuelList(generics.ListAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer


class FuelDetail(generics.RetrieveAPIView):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer


class AZSFuelList(generics.ListAPIView):
    queryset = AZSFuel.objects.all()
    serializer_class = AZSFuelSerializer


class AZSFuelDetail(generics.RetrieveAPIView):
    queryset = AZSFuel.objects.all()
    serializer_class = AZSFuelSerializer
