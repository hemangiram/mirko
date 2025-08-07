from rest_framework import serializers
from .models import Testimation




class TestimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimation
        fields = '__all__'