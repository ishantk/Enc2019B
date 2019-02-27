import pandas as pd

table = pd.read_csv("CityTemps.csv")
print(table)

print("====")

print(table["Year"])

print("====")

print(table.iloc[1])

print("=====")

print(table.iloc[1:5])

# table = pd.read_excel()
# table = pd.read_json()

#Assignemnt: Explore Pandas on Different DataSets (Create DataFrames) from Kaggle or Government Portals