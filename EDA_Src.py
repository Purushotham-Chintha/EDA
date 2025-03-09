import chardet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir,"Downloads", "Sample - Superstore.csv")

with open(file_path, "rb") as f:
    rawdata = f.read()
    result = chardet.detect(rawdata)

"""print(result)""" # Detects the best encoding

df = pd.read_csv(file_path, encoding = result["encoding"])
print(df.sample(40))

print(df.info())

print(df.sample(10))

print(df.dtypes)

print(df.describe())