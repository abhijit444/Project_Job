from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from StockAPI.views import IndexesViewSet, DailyPricesViewSet

router = DefaultRouter()
router.register(r'indexes', IndexesViewSet)
router.register(r'daily-prices', DailyPricesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('daily-prices/<int:pk>/prices-for-date/', DailyPricesViewSet.as_view({'get': 'prices_for_date'}),
         name='daily-prices-prices-for-date'),  # Custom path for fetching prices for a specific date
    path('daily-prices/', DailyPricesViewSet.as_view({'get': 'list'}),
         name='daily-prices-list'),  # Custom path for listing daily prices with filtering options
    path('indexes/<int:pk>/first-five/', IndexesViewSet.as_view({'get': 'first_five'}),
         name='indexes-first-five'),  # Custom path for fetching the first five indexes
] + router.urls
