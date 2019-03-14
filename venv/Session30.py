# DecisionTreeClassifier Implementation

"""
    Data

    Attributes for Vehicle which can classify 2W and 4W

        weight
        engine

        Bike | 0
        100kgs     100cc
        150kgs     110cc
        180kgs     150cc
        200kgs     180cc

        Car | 1
        800kgs     1000cc
        1000kgs    1200cc
        1200kgs    1300cc
        1500kgs    1500cc

"""

from sklearn import tree
# Representation of Data as Features
data = [[100,100], [150,110], [180,150], [200,180],[800,1000], [1000,1200], [1200,1300], [1500,1500]]
# Labels
output = [0, 0, 0, 0, 1, 1, 1, 1]

clf = tree.DecisionTreeClassifier()
clf.fit(data, output) # Supervised Learning

input = [[1110, 1222]]
label = clf.predict(input)
print(label)

if label[0] is 0:
    print("Its a Bike")
else:
    print("Its a Car")

# Class Assignment : Classify Human and Animals.
#                    Classify Fruits and Vegetables