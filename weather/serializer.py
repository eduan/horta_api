from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather

    def create(self, validated_data):
        return Weather(**validated_data)