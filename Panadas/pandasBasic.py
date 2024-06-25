import pandas as pd
# MANUALLY ADDING DATA AND THEN READING
# data = {"Name":["Aditya", "Ayush", "Abhinav"], "Age":[25, 27, 31], "Salary":[30000, 25000, 25000]}
# df = pd.DataFrame(data)
# print(df)
# print()



# READING DATA FROM RANDOM EXCELSHEET
data2 = pd.read_excel("C:/Users/apeks/Downloads/pandas_Trial.xlsx")
# print(data2)
# print(data2.head(10))
# print(data2.tail(10))

# print(data2.info())
# print(data2.describe())  #ye jitne bhi numerical columns hai vo find krenga aur unke uper diffrent functions perform krega

print(data2.isnull().sum()) # ye jitni bhi null values hai apne data k andar vo nikal kr de denga aur sum() unka total

