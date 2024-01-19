from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .models import Indexes, DailyPrices
from .serializers import IndexesSerializer, DailyPricesSerializer

class IndexesViewSet(viewsets.ModelViewSet):
    queryset = Indexes.objects.all()
    serializer_class = IndexesSerializer

class DailyPricesFilter(filters.FilterSet):
    date__gte = filters.DateFilter(field_name='date', lookup_expr='gte')
    date__lte = filters.DateFilter(field_name='date', lookup_expr='lte')
    open_price__gte = filters.NumberFilter(field_name='open_price', lookup_expr='gte')
    high_price__gte = filters.NumberFilter(field_name='high_price', lookup_expr='gte')
    low_price__gte = filters.NumberFilter(field_name='low_price', lookup_expr='gte')
    close_price__gte = filters.NumberFilter(field_name='close_price', lookup_expr='gte')
    shares_traded__gte = filters.NumberFilter(field_name='shares_traded', lookup_expr='gte')
    turnover__gte = filters.NumberFilter(field_name='turnover', lookup_expr='gte')

    class Meta:
        model = DailyPrices
        fields = []

class DailyPricesViewSet(viewsets.ModelViewSet):
    queryset = DailyPrices.objects.all()
    serializer_class = DailyPricesSerializer
    filterset_class = DailyPricesFilter

    @action(detail=True, methods=['get'])
    def prices_for_date(self, request, pk=None):
        """Retrieve daily prices for a specific date."""
        index = self.get_object()
        date = request.query_params.get('date')
        prices = DailyPrices.objects.filter(index=index, date=date)
        serializer = self.get_serializer(prices, many=True)
        return Response(serializer.data)
