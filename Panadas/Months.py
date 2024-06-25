import pandas as pd

data = {"Months": ["January", "February", "March", "April"]}
a = pd.DataFrame(data)
print(a)

def extract(value):
    return value[0:3]

a["Short_months"] = a["Months"].map(extract)
print(a)