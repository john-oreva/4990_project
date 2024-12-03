import yfinance as yf
import pandas as pd


ticker_symbol = '^GSPTSE'


start_date = '1999-01-01'
end_date = '2024-12-02'


data = yf.download(ticker_symbol, start=start_date, end=end_date, interval='1mo')


csv_file_path = 'GSPTSE_historical_data.csv'
data.to_csv(csv_file_path)

print(f"Data successfully saved to {csv_file_path}")
