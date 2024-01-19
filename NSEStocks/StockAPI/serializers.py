from rest_framework import serializers
from .models import Indexes, DailyPrices

class IndexesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indexes
        fields = '__all__'

class DailyPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrices
        fields = '__all__'
