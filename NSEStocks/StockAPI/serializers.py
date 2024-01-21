from rest_framework import serializers
from .models import Index, DailyPrice

class DailyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrice
        fields = '__all__'

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = '__all__'
        