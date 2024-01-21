# Generated by Django 5.0.1 on 2024-01-20 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockAPI', '0006_csvupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shares_traded', models.BigIntegerField()),
                ('turnover', models.DecimalField(decimal_places=2, max_digits=15)),
                ('csv_file', models.FileField(upload_to='daily_Prices_csv/')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='CsvUpload',
        ),
        migrations.AddField(
            model_name='dailyprice',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_prices', to='StockAPI.index'),
        ),
        migrations.DeleteModel(
            name='DailyPrices',
        ),
        migrations.DeleteModel(
            name='Indexes',
        ),
    ]