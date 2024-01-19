from django.db import models

class Indexes(models.Model):
    name = models.CharField(max_length=100)

class DailyPrices(models.Model):
    index = models.ForeignKey(Indexes, on_delete=models.CASCADE, related_name='daily_prices')
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()

