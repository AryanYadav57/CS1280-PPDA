import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Ram', 'Robert','Rahim'],
'Age': [25, 30, 35],
'City': ['Ayodya', 'Chennai', 'Delhi']}
df = pd.DataFrame(data)
print(df)

# Access a column
print(df["Name"])
# Accessing a row by label
print(df.loc[0])
# Access a row by index
print(df.iloc[1])
# Access a specific cell
print(df.at[0, "Age"])
# Slicing
print(df[1:3]) # Slicinp

print(df.at[2,"City"])