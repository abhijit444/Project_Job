# management/commands/import_nse_data.py
from django.core.management.base import BaseCommand
from StockAPI.models import Indexes, DailyPrices
import pandas as pd
import requests
from io import StringIO
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Add user-agent headers to mimic a browser
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        # Download CSV data
        url = 'https://www.nseindia.com/reports-indices-historical-index-data'
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses
        except requests.RequestException as e:
            logger.error(f"Failed to fetch data from NSE website: {e}")
            return

        # Parse CSV data
        try:
            csv_data = StringIO(response.text)
            df = pd.read_csv(csv_data)
        except pd.errors.EmptyDataError:
            logger.warning("Received empty CSV data from NSE website.")
            return
        except pd.errors.ParserError as e:
            logger.error(f"Failed to parse CSV data: {e}")
            return

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

        logger.info("Data import completed successfully.")