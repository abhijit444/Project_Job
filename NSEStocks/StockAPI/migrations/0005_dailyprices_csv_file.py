# Generated by Django 5.0.1 on 2024-01-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockAPI', '0004_remove_dailyprices_csv_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyprices',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to='DailyPrices_csv/'),
        ),
    ]