import os
import pandas as pd
import matplotlib.pyplot as plt

file_name = "14100355.csv"  
output_csv = "filtered_employment_finance_1995_2024.csv"
industry_column = "North American Industry Classification System (NAICS)"
industry_name = "Finance, insurance, real estate, rental and leasing [52-53]"
start_date = "1995-01-01"
end_date = "2024-01-01"


if not os.path.exists(file_name):
    print(f"The file {file_name} does not exist. Please download and extract the data.")
    exit()
else:
    print(f"Using existing file: {file_name}")


if os.path.exists(output_csv):
    print(f"Filtered file '{output_csv}' already exists. Skipping data processing.")
    filtered_data = pd.read_csv(output_csv)  
    filtered_data['REF_DATE'] = pd.to_datetime(filtered_data['REF_DATE'])  
else:
    print("Processing data...")
    try:
        data = pd.read_csv(file_name, low_memory=False)  
        print("Columns in the dataset:", data.columns)
    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        exit()


    data['REF_DATE'] = pd.to_datetime(data['REF_DATE'])

 
    filtered_data = data[
        (data[industry_column] == industry_name) &  
        (data['REF_DATE'] >= start_date) &         
        (data['REF_DATE'] <= end_date)             
    ]

   
    if filtered_data.empty:
        print("No data available for the specified range and industry.")
        exit()


    filtered_data.to_csv(output_csv, index=False)
    print(f"Filtered data saved to {output_csv}.")

