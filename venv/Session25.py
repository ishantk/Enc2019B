import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("FullData.csv")
# print(df)

# print(df.head(5))
# print(df.tail(5))

# print(df["Nationality"])
# print(df.Nationality)

"""
plt.figure(figsize=(30,20))
sns.countplot(y=df.Nationality, palette="Set2")
plt.show()
"""

"""
plt.figure(figsize=(15,10))
sns.countplot(x="Age", data=df)
plt.show()
"""
# Case Study : Find Goalkeeper who is strongest to stop the shots

# print(df["GK_Handling"])
# print(df.GK_Handling)

# Create some weights as per the importance of Attribute
w1 = 1
w2 = 1
w3 = 1
w4 = 3
w5 = 4

df["GK_Shot_Stopper"] = (w1*df.GK_Positioning + w2*df.GK_Diving + w3*df.GK_Kicking + w4*df.GK_Handling + w5*df.GK_Reflexes)
# print(df["GK_Shot_Stopper"])

sortedDf = df.sort_values("GK_Shot_Stopper")
# print(sortedDf)
print(sortedDf.head(5))
print()
print(sortedDf.tail(5)) # Best 5 GoalKeepers

# Assignment : Get the dataset for Indian Cricket (IPL) Kaggle
#              Analyze and tell who are the best cricketers overall -> Top 10
#              Best Batsmen -> Top 10
#              Best Bowlers -> Top 10
#              Best WC      -> Top 5


"""
filteredDf = sortedDf.tail(5)

plt.figure(figsize=(15,10))
sns.countplot(x="Nationality", data=filteredDf)
plt.show()
"""
