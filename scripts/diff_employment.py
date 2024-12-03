import pandas as pd
import matplotlib.pyplot as plt


file_name = "filtered_employment_finance_1995_2024.csv"


filtered_data = pd.read_csv(file_name)
filtered_data['REF_DATE'] = pd.to_datetime(filtered_data['REF_DATE'])  # Ensure datetime format

tech_bubbles = [
    {"name": "Tech Bubble 1.0", "start": "1995-01-01", "end": "2005-12-31"},
    {"name": "Tech Bubble 2.0", "start": "2008-01-01", "end": "2015-12-31"},
    {"name": "Tech Bubble 3.0", "start": "2020-01-01", "end": "2024-01-01"},
]


filtered_data['Bubble'] = 'Outside Bubbles'  
for bubble in tech_bubbles:
    start = pd.Timestamp(bubble["start"])
    end = pd.Timestamp(bubble["end"])
    filtered_data.loc[(filtered_data['REF_DATE'] >= start) & (filtered_data['REF_DATE'] <= end), 'Bubble'] = bubble["name"]


pivot_data = filtered_data.pivot_table(
    index='REF_DATE',
    columns='Bubble',
    values='VALUE',
    aggfunc='sum'
).fillna(0)


plt.figure(figsize=(14, 8))
plt.stackplot(
    pivot_data.index,
    pivot_data.values.T,
    labels=pivot_data.columns,
    alpha=0.8
)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Employees (x 1,000)', fontsize=12)
plt.title('Employment Trends in Finance Industry During Tech Bubbles (1995–2024)', fontsize=14)
plt.legend(loc='upper left', fontsize=10, title='Tech Bubbles')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.savefig('employment_trends_stacked_area_chart.png')
plt.show()
