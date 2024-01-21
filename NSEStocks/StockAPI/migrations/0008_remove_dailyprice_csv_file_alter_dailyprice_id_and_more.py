# Generated by Django 5.0.1 on 2024-01-20 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockAPI', '0007_dailyprice_index_delete_csvupload_dailyprice_index_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyprice',
            name='csv_file',
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='index',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='csv_files/')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csv_files', to='StockAPI.index')),
            ],
        ),
    ]
