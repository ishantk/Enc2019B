"""
    DataSet

    Attributes for Vehicle which can classify 2W and 4W

        weight
        engine

        Weight(Y)   Engine(X)   Vehicle(Output)
        100kgs     100cc           Bike
        150kgs     110cc           Bike
        1200kgs    1300cc          Car
        180kgs     150cc           Bike
        800kgs     1000cc          Car
        200kgs     180cc           Bike
        1000kgs    1200cc          Car
        1500kgs    1500cc          Car

        Bike -> 0
        Car ->  1

        1. numpy
        2. scipy
        3. sklearn

"""

from sklearn.naive_bayes import GaussianNB
import numpy as np

# from sklearn import svm   # Refer scikit.org | Use IRIS Data Set

FEATURES = np.array([ [100,100], [150,110], [1200,1300], [180,150], [800,1000], [200,180], [1000, 1200], [1500,1500] ])
LABELS = np.array([0, 0, 1, 0, 1, 0, 1, 1])

model = GaussianNB()
model.fit(FEATURES, LABELS)

dataToPredict = [110, 90]

output = model.predict([dataToPredict])
print("Prediction is:",output)

