from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from StockAPI.views import IndexesViewSet, DailyPricesViewSet

router = DefaultRouter()
router.register(r'indexes', IndexesViewSet)
router.register(r'daily-prices', DailyPricesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

