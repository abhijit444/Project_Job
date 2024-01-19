# admin.py
from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Indexes, DailyPrices

class DailyPricesAdmin(admin.ModelAdmin):
    list_display = ['index', 'date', 'csv_file']
    actions = ['export_csv', 'import_csv']

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

    def import_csv(self, request):
        # Handle file upload
        if 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            # Process the uploaded CSV file here (you can use csv.reader or pandas)
            # Update the code based on your CSV structure and model fields
            # For simplicity, assuming CSV has the same structure as export
            csv_data = csv.reader(csv_file.read().decode('utf-8').splitlines())
            next(csv_data)  # Skip header row
            for row in csv_data:
                Indexes.objects.get_or_create(name=row[0])  # Assuming Indexes already exist
                DailyPrices.objects.create(
                    index=Indexes.objects.get(name=row[0]),
                    date=row[1],
                    open_price=row[2],
                    high_price=row[3],
                    low_price=row[4],
                    close_price=row[5],
                    shares_traded=row[6],
                    turnover=row[7],
                )
            self.message_user(request, f'Successfully imported data from CSV file: {csv_file.name}')

    import_csv.short_description = 'Import data from CSV file'

    def get_actions(self, request):
        actions = super().get_actions(request)
        custom_actions = {
            'export_csv': (self.export_csv, 'export_csv', 'Export selected daily prices to CSV'),
            'import_csv': (self.import_csv, 'import_csv', 'Import data from CSV file'),
        }
        actions.update(custom_actions)
        return actions

class IndexesAdmin(admin.ModelAdmin):
    list_display = ['name', 'csv_file']

admin.site.register(Indexes, IndexesAdmin)
admin.site.register(DailyPrices, DailyPricesAdmin)
