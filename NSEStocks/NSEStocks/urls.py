from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from StockAPI.views import IndexesViewSet, DailyPricesViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'indexes', IndexesViewSet)
router.register(r'daily-prices', DailyPricesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

