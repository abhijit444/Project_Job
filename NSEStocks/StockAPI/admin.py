from django.contrib import admin
from .models import Indexes, DailyPrices


@admin.register(Indexes)
class IndexesAdmin(admin.ModelAdmin):
    pass

@admin.register(DailyPrices)
class DailyPricesAdmin(admin.ModelAdmin):
    pass
