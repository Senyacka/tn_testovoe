from rest_framework import serializers
from azs_fuel.models import Fuel, AZSFuel


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = "__all__"


class AZSFuelSerializer(serializers.ModelSerializer):
    fuel_name = serializers.SerializerMethodField(allow_null=True)
    fuel_price = serializers.SerializerMethodField(allow_null=True)
    fuel_currency = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = AZSFuel
        fields = ['azs', 'id', 'fuel_name', 'fuel_price', 'fuel_currency']

    def get_fuel_name(self, instance: AZSFuel):
        return instance.fuel.name

    def get_fuel_price(self, instance):
        return instance.fuel.fuel_price

    def get_fuel_currency(self, instance):
        return instance.fuel.currency
