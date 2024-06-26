# Generated by Django 5.0.1 on 2024-01-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockAPI', '0005_dailyprices_csv_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csv_uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
