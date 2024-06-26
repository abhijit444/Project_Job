# Generated by Django 5.0.1 on 2024-01-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyprices',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to='daily_prices_csv/'),
        ),
        migrations.AddField(
            model_name='indexes',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to='indexes_csv/'),
        ),
    ]
