
import pandas as pd

class AddName:
    def add(self):
      data = pd.read_csv("employeeName.csv")
      data["Full Name"] = data["First Name"].str.capitalize() + " " + data["Last Name"].str.capitalize()
      print(data)
      print()
      data2 = data.copy()
      data2.to_csv("newEmployee.csv")
      print(data2)

    def __init__(self, file_path):
        self.file_path = file_path

obj = AddName("employeeName.csv")
obj.add()



















