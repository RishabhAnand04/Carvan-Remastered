from rest_framework import serializers
from .models import Places,Visiting

class PlacesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'

class VisitingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visiting
        fields = '__all__'