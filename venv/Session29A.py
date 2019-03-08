def dataGenerator():
    file = "CityTemps.csv"
    for row in open(file, "r"):
        # print(row)
        yield row

# dataGenerator()
dg = dataGenerator()
print(next(dg))
print(next(dg))
print(next(dg))