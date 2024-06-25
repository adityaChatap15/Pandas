import pandas as pd
data = pd.read_excel("C:/Users/apeks/Downloads/pandas_2Trial.xlsx")
# print(data)

data.loc[(data["Bonus"] == 0), "GetBonus"] = "No Bonus"  #isme phle ek "GetBonus naam se new column ban jyengi then jinka bhi bonus 0 ho uske correspoding nobunus store ho jyenga getbonus me
data.loc[(data["Bonus"] > 0), "GetBonus"] = "Bonus" #isme jinka 0 se jyda ho vha Bonus store ho jyenga
print(data)

#  Yha pr hum 2 columns ko add krke ek new columns bana rhe hai
# yha pr first name aur last name ko add kr rhe hai aur first name aur last name k first character ko capital bna rhe hai
data["Full Name"] = data["First Name"].str.capitalize() + " " + data["Last Name"].str.capitalize()
print(data)