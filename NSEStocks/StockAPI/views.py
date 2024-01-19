from django.shortcuts import render
from rest_framework import viewsets
from .models import Indexes, DailyPrices
from .serializers import IndexesSerializer, DailyPricesSerializer

class IndexesViewSet(viewsets.ModelViewSet):
    queryset = Indexes.objects.all()
    serializer_class = IndexesSerializer

class DailyPricesViewSet(viewsets.ModelViewSet):
    queryset = DailyPrices.objects.all()
    serializer_class = DailyPricesSerializer

