import numpy as np
import pandas as pd

# Create a list of dictionaries representing product information
products = [
    {"Product Name": "Laptop", "Category": "Electronics", "Price": 1000},
    {"Product Name": "Phone", "Category": "Electronics", "Price": 500},
    {"Product Name": "Chair", "Category": "Furniture", "Price": 150},
    {"Product Name": "Table", "Category": "Furniture", "Price": 300},
    {"Product Name": "Headphones", "Category": "Electronics", "Price": 200}
]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(products)

# Add a new column for discounted price (90% of original price)
df["Discounted Price"] = df["Price"] * 0.9

# Display the DataFrame
print(df)
