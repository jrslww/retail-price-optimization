import pandas as pd
from sklearn.preprocessing import LabelEncoder

## Function to load the processed dataset
def load_processed_data(data_path):
    data = pd.read_csv(data_path)
    return data

## Function to save the engineered dataset
def save_engineered_data(data, output_path):
    data.to_csv(output_path, index=False)

# Load the processed dataset
data_path = "../data/processed_data.csv"
data = load_processed_data(data_path)

# Calculate the average price per product
avg_price_per_product = data.groupby('StockCode')['UnitPrice'].mean().reset_index()
avg_price_per_product.columns = ['StockCode', 'AvgPrice']
data = data.merge(avg_price_per_product, on='StockCode')

# Calculate the price difference between the current price and the average price
data['PriceDiff'] = data['UnitPrice'] - data['AvgPrice']

# One-hot encoding for the 'Description' column
description_dummies = pd.get_dummies(data['Description'], prefix='Description')
data = pd.concat([data, description_dummies], axis=1)
data = data.drop('Description', axis=1)

# Label encoding for the 'Country' column
encoder = LabelEncoder()
data['Country'] = encoder.fit_transform(data['Country'])

# Save the engineered dataset
output_path = "../data/engineered_data.csv"
save_engineered_data(data, output_path)
