# models.py
# models.py
from django.db import models

class Index(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DailyPrice(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, related_name='daily_prices')
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    shares_traded = models.BigIntegerField()
    turnover = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.index.name} - {self.date}"

class CSVFile(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, related_name='csv_files')
    file = models.FileField(upload_to='csv_files/')

    def __str__(self):
        return f"{self.index.name} - {self.file.name}"


