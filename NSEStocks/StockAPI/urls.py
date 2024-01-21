
from django.urls import path
from .views import IndexList, DailyPriceList, index_detail

urlpatterns = [
    path('indexes/', IndexList.as_view(), name='index-list'),
    path('indexes/<int:index_id>/', index_detail, name='index-detail'),
    path('indexes/<int:index_id>/prices/', DailyPriceList.as_view(), name='daily-price-list'),
]
