import pandas as pd

data = pd.read_excel("C:/Users/apeks/Downloads/pandas_2Trial.xlsx")
print(data)

# print(data["EEID"].duplicated().sum()) # ye jitne dupliacate hai utne elements ka sum de denga

print(data.drop_duplicates("EEID"))  # Hamesha ase column k basis pr drop krna jo unique hona cheya jaise ki primary key k basis pr
