import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_stock_data(ticker, start_date, end_date, filename):
    data = yf.download(ticker, start=start_date, end=end_date, interval='1mo')
    data.to_csv(filename)
    return data


ticker_symbol = '^GSPTSE' 
data_1_0 = fetch_stock_data(ticker_symbol, '1995-01-01', '2005-12-31', 'TSX_1995_2005.csv')


data_1_0['Close'].plot(title="TSX Composite Index (1995-2005)")
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.savefig('TSX_1995_2005_trends.png')
plt.show()
