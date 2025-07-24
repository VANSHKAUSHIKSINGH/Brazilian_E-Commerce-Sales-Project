import pandas as pd
from sqlalchemy import create_engine


# MySQL connection parameters

user = 'root'
password = 'Kaushik%409654016'  # If We use @ in password, we need to escape it as %40 for '@' for engine connection.
host = 'localhost'
port = '3306'
database = 'Brazil_Ecommerce'



# Create MySQL SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

# Path to your CSV folder
csv_path = 'D:/Datasets/'  # Change this to where your CSVs are stored

# Mapping of table names to CSV files
table_files = {
    'customers': 'olist_customers_dataset.csv',
    'geolocation': 'olist_geolocation_dataset.csv',
    'order_items': 'olist_order_items_dataset.csv',
    'order_payments': 'olist_order_payments_dataset.csv',
    'order_reviews': 'olist_order_reviews_dataset.csv',
    'orders': 'olist_orders_dataset.csv',
    'products': 'olist_products_dataset.csv',
    'sellers': 'olist_sellers_dataset.csv',
    'Categories_name' : 'product_category_name_translation.csv'
}   

for table, filename in table_files.items():
    try:
        print(f"importing {table} from {filename}...")
        df = pd.read_csv(csv_path + filename)
        df.to_sql(name=table, con=engine, if_exists='replace', index=False)
        print(f" Successfully imported `{table}` with {df.shape[0]} rows\n")
    except Exception as e:
        print(f" Failed to import {filename}: {e}")

print("🎉 All available CSVs have been processed.")
    
