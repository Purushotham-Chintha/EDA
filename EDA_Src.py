import chardet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, "Downloads", "Sample - Superstore.csv")

with open(file_path, "rb") as f:
    rawdata = f.read()
    result = chardet.detect(rawdata)

"""print(result)"""  # Detects the encoding of our dataset

df = pd.read_csv(file_path, encoding=result["encoding"])

# Print the shape of the dataframe (r * c)
print(df.shape)

# Print the information about the dataframe
print(df.info())

# Select the top 10 rows of dataframe
print(df.head(10))

# Select the bottom 10 rows of a dataframe
print(df.tail(10))

# Select the 10 random rows of a dataframe
print(df.sample(10))

# Drop all the duplicate rows from the dataframe
df = df.drop_duplicates()  # Returns a dataframe with duplicates removed

"""df.drop_duplicates(inplace=True)"""  # modify the DataFrame rather than creating a new one.

# print(df.dtypes)
#
# print(df.describe())
#
# print(df.isnull)

# print(df.sample(40))

"""date parsing from string format to datetime object  allowing for
specific date operations"""

df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# select and check the type of ship date column
Ship_Date = df["Ship Date"]
# print(Ship_Date)
