import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_stock_data(ticker, start_date, end_date, filename):
   
    data = yf.download(ticker, start=start_date, end=end_date, interval='1mo')
    
    
    if data.empty:
        print(f"No data fetched for {ticker} from {start_date} to {end_date}.")
        return None
    
    
    data.to_csv(filename)
    print(f"Data successfully saved to {filename}.")
    return data


ticker_symbol = '^GSPTSE'
start_date_3 = '2020-01-01'
end_date_3 = '2024-12-01'
filename_3 = 'TSX_TechBubble3_2020_2024.csv'

data_3 = fetch_stock_data(ticker_symbol, start_date_3, end_date_3, filename_3)


if data_3 is not None:
    
    data_3['Close'] = data_3['Close'].interpolate()

    plt.figure(figsize=(10, 6))
    data_3['Close'].plot(title="TSX Composite Index Performance (2020–2024)", color='green')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (CAD)')
    plt.grid()
    plt.savefig('TSX_TechBubble3_2020_2024_trends.png')
    plt.show()
else:
    print("No plot generated due to missing data.")
