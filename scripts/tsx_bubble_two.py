import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_stock_data(ticker, start_date, end_date, filename):
    data = yf.download(ticker, start=start_date, end=end_date, interval='1mo')
    data.to_csv(filename)
    return data


ticker_symbol = '^GSPTSE'  
start_date_2 = '2008-01-01'
end_date_2 = '2015-12-31'
filename_2 = 'TSX_TechBubble2_2008_2015.csv'

data_2 = fetch_stock_data(ticker_symbol, start_date_2, end_date_2, filename_2)


plt.figure(figsize=(10, 6))
data_2['Close'].plot(title="TSX Composite Index Performance (2008–2015)", color='blue')
plt.xlabel('Date')
plt.ylabel('Closing Price (CAD)')
plt.grid()
plt.savefig('TSX_TechBubble2_2008_2015_trends.png')
plt.show()
