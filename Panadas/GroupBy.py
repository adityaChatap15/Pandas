import pandas as pd

data = pd.read_excel("C:/Users/apeks/Downloads/pandas_2Trial.xlsx")
print(data)

# gp1 = data.groupby("Department").agg({"EEID":"count"})
# print(gp1)

gp2 = data.groupby(["Department", "Gender"]).agg({"EEID":"count"})
print(gp2)