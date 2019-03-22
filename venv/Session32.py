from sklearn.datasets import load_iris
from sklearn import tree
import graphviz

irisData = load_iris()
# print("====DataSet====")
# print(irisData)

print("====Data====")
print(irisData.data)

print("====Target====")
print(irisData.target)

print("====Names====")
print(irisData.target_names)

classifier = tree.DecisionTreeClassifier()
classifier.fit(irisData.data, irisData.target)

inputData = [7.7, 3.8, 6.7, 2.2]
predictedClass = classifier.predict([inputData])
print("Flower Class Predicted:", predictedClass)
print("Flower Class Predicted:", predictedClass[0])
print("Flower Class Predicted:", irisData.target_names[predictedClass[0]])

# export_graphviz -> Takes inputs !!
data = tree.export_graphviz(classifier, out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATA-SET TREE")
graph.view()