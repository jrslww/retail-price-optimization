import pandas as pd

def load_data(data_path):
    data = pd.read_excel(data_path)
    return data

def preprocess_data(data):
    data = data.dropna(subset=['CustomerID'])
    data = data[data['Quantity'] > 0]
    data['Revenue'] = data['Quantity'] * data['UnitPrice']
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    data['Year'] = data['InvoiceDate'].dt.year
    data['Month'] = data['InvoiceDate'].dt.month
    data['Day'] = data['InvoiceDate'].dt.day
    data['Weekday'] = data['InvoiceDate'].dt.weekday
    data = data.drop('InvoiceDate', axis=1)
    return data

def save_processed_data(data, output_path):
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = "../data/Online Retail.xlsx"
    output_path = "../data/processed_data.csv"

    raw_data = load_data(input_path)
    processed_data = preprocess_data(raw_data)
    save_processed_data(processed_data, output_path)