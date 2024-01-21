import os
import csv
from django.core.management.base import BaseCommand
from StockAPI.models import DailyPrice
from datetime import datetime

class Command(BaseCommand):
    help = 'Import daily prices data from CSV files in a directory'

    def add_arguments(self, parser):
        parser.add_argument('folder_path', type=str, help='Path to the folder containing CSV files')

    def handle(self, *args, **kwargs):
        folder_path = kwargs['folder_path']

        # Check if the specified path is a directory
        if not os.path.isdir(folder_path):
            self.stderr.write(self.style.ERROR(f'The provided path "{folder_path}" is not a directory.'))
            return

        # Get a list of all CSV files in the directory
        csv_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.csv')]

        if not csv_files:
            self.stdout.write(self.style.SUCCESS(f'No CSV files found in the specified directory: {folder_path}'))
            return

        # Process each CSV file in the directory
        for csv_file_name in csv_files:
            csv_file_path = os.path.join(folder_path, csv_file_name)

            with open(csv_file_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    try:
                        date_str = row['Date']
                        date = datetime.strptime(date_str, '%d-%b-%y').date()  # Adjust the date format as needed

                        DailyPrice.objects.create(
                            index_id=row['Index'],  # Assuming 'Index' is the field name for the Index name
                            date=date,
                            open_price=float(row['Open']),
                            high_price=float(row['High']),
                            low_price=float(row['Low']),
                            close_price=float(row['Close']),
                            shares_traded=int(row['Shares Traded']),
                            turnover=float(row['Turnover (â‚¹ Cr)']),  # Adjust the field name
                        )
                    except KeyError as e:
                        self.stderr.write(self.style.ERROR(f'Missing key in CSV file: {e}'))

            self.stdout.write(self.style.SUCCESS(f'Data from file {csv_file_name} imported successfully'))
