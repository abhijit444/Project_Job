from django.db import models

class Indexes(models.Model):
    name = models.CharField(max_length=100)
    csv_file = models.FileField(upload_to='indexes_csv/', null=True, blank=True)

class DailyPrices(models.Model):
    index = models.ForeignKey(Indexes, on_delete=models.CASCADE, related_name='daily_prices')
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()
    csv_file = models.FileField(upload_to='daily_prices_csv/', null=True, blank=True)
