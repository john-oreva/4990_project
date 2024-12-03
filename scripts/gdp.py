import pandas as pd
import matplotlib.pyplot as plt


file_path = '3610043401.csv'
df_cleaned = pd.read_csv(file_path, skiprows=10, header=1)


financial_gdp = df_cleaned[df_cleaned.iloc[:, 0] == 'Finance and insurance  [52]']


financial_gdp = financial_gdp.dropna(axis=1, how='all')  
financial_gdp = financial_gdp.iloc[:, 1:] 


months = list(financial_gdp.columns)
financial_gdp = financial_gdp.T  


financial_gdp.columns = ['GDP']
financial_gdp['Date'] = pd.date_range(start="1997-01", periods=len(financial_gdp), freq='M')
financial_gdp['GDP'] = financial_gdp['GDP'].str.replace(',', '').astype(float)  # Convert to numeric


financial_gdp.reset_index(drop=True, inplace=True)


plt.figure(figsize=(12, 6))
plt.plot(financial_gdp['Date'], financial_gdp['GDP'], label='Financial Industry GDP', color='blue')
plt.title('GDP Contribution Trend of Financial Industry (1997-Present)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('GDP (Millions of CAD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
