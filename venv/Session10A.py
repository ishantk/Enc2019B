# ldhPopulation = 12341
# jalPopulation = 45673
# mhPopulation = 12121
# asrPopulation = 78221
# fzrPopulation = 90875

# populationCount = ldhPopulation + jalPopulation + mhPopulation + asrPopulation + fzrPopulation

"""
punjabPopulation = [12341, 45673, 12121, 78221, 90875]
haryanaPopulation = [22341, 55673, 32121, 88221, 80875]

popCount1 = 0
popCount2 = 0

for num in punjabPopulation:
    popCount1 = popCount1 + num

for num in haryanaPopulation:
    popCount2 = popCount2 + num

print("Population of Punjab is",popCount1)
print("Population of Haryana is",popCount2)
"""

# List of Lists
indiaPopulation = [ [12341, 45673, 12121, 78221, 90875],
                    [22341, 55673, 32121, 88221],
                    [22341, 55673, 32121, 88221, 67865, 142461],]
print(len(indiaPopulation))
print(len(indiaPopulation[0]))
print(len(indiaPopulation[1]))
print(indiaPopulation[0])
print(indiaPopulation[1])

print(indiaPopulation[0][0])
print(indiaPopulation[1][2])

populationCounts = []

for i in range(0, len(indiaPopulation)):
    total = 0
    for j in range(0, len(indiaPopulation[i])):
        total = total + indiaPopulation[i][j]

    # print("For i:",i,"Total is:",total)
    populationCounts.append(total)

print(indiaPopulation)
print(populationCounts)

# Class Assignment : Find Maximum Population !! 0th state or 1st state or 2nd state
for p in populationCounts:
    print(p)