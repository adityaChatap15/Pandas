import pandas as pd
import numpy as np

data = pd.read_excel("C:/Users/apeks/Downloads/pandas_2Trial.xlsx")
# print(data)

# print(data.isnull().sum())

# print(data.replace(np.nan, 30000))   # If we directly use replace for null value then vo har jagha same vaalue fill kr denga

# data["Salary"] = data["Salary"].replace(np.nan, 32000)  # Ye bss jha salary ki value null hongi vha pr bss change krenga
# print(data)

m = data["Salary"].mean()//1
data["Salary"] = data["Salary"].replace(np.nan, m) # yha pr ham mean value put kr rhe hai null salary ki jagha pr
# print(data)

# print(data.fillna(method="bfill")) # ye null k niche vaali values ko null me fill kr denga

# print(data.fillna(method="ffill"))  # ye uper vaali values ko null m fill kr denga
