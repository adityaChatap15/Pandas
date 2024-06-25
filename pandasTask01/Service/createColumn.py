import pandas as pd

df_employee = pd.DataFrame({
    'First Name': ['aditya', 'ayush', 'abhinav'],
    'Last Name': ['chatap', 'tiwari', 'sharma']
})
df_employee.to_csv("employeeName.csv")



