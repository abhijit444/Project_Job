# admin.py
from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Indexes, DailyPrices

class DailyPricesAdmin(admin.ModelAdmin):
    actions = ['export_csv']

    def export_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="daily_prices.csv"'
        writer = csv.writer(response)
        writer.writerow(['Indexes', 'Date', 'Open', 'High', 'Low', 'Close', 'Shares Traded', 'Turnover'])
        for daily_price in queryset:
            writer.writerow([daily_price.index.name, daily_price.date, daily_price.open_price,
                             daily_price.high_price, daily_price.low_price, daily_price.close_price,
                             daily_price.shares_traded, daily_price.turnover])
        return response

    export_csv.short_description = 'Export selected daily prices to CSV'


class IndexesAdmin(admin.ModelAdmin):
    list_display = ['name', 'csv_file']

class DailyPricesAdmin(admin.ModelAdmin):
    list_display = ['index', 'date', 'csv_file']

admin.site.register(Indexes, IndexesAdmin)
admin.site.register(DailyPrices, DailyPricesAdmin)

