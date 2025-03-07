import pandas as pd
import numpy as np

# Create a Series from a list
data = [1, 3, 5, np.nan, 6]
s = pd.Series(data)
print(s)

# To print the type of the first element in the list (data[0])
print(type(data[0]))  # This will print the type of the first element