from rest_framework import serializers
from .models import Index, DailyPrice

class IndexesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indexes
        fields = '__all__'

class DailyPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPrices
        fields = '__all__'
