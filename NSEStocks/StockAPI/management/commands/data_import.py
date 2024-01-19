# management/commands/import_nse_data.py
from django.core.management.base import BaseCommand
from StockAPI.models import Indexes, DailyPrices
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Specify the path to your local directory containing CSV files
        data_directory = 'C:/Users/avina/Desktop/Stock Market'  # Replace with your actual directory path

        # Check if the directory exists
        if not os.path.exists(data_directory):
            logger.error(f"Directory not found at: {data_directory}")
            return

        # Loop through all CSV files in the directory
        for filename in os.listdir(data_directory):
            if filename.endswith('.csv'):
                file_path = os.path.join(data_directory, filename)

                # Parse CSV data from the local file
                try:
                    df = pd.read_csv(file_path)
                except pd.errors.EmptyDataError:
                    logger.warning(f"Received empty CSV data from the file: {filename}")
                    continue
                except pd.errors.ParserError as e:
                    logger.error(f"Failed to parse CSV data from the file {filename}: {e}")
                    continue

                # Create indexes and daily prices
                for index_name, group in df.groupby('Indexes'):
                    index = Indexes.objects.get_or_create(name=index_name)[0]
                    for _, row in group.iterrows():
                        DailyPrices.objects.create(
                            index=index,
                            date=row['Date'],
                            open_price=row['Open'],
                            high_price=row['High'],
                            low_price=row['Low'],
                            close_price=row['Close'],
                            shares_traded=row['Shares Traded'],
                            turnover=row['Turnover'],
                        )

                logger.info(f"Data import from file {filename} completed successfully.")


