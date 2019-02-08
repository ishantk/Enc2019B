# returns a list representing the binary form of N
def getBinaryRep(N):
    bitList = []
    while N != 0:
	    # determine the least significant bit and add to bitList
        if N%2 == 1:
            bitList = [1] + bitList
        else:
            bitList = [0] + bitList
	    # remove the least significant bit
        N = N//2
    return bitList


NumOfItems = 6
AllSubsets = []
for i in range(2**NumOfItems):
	# using the function from previous slide
    subset = getBinaryRep(i)
	# add zeroes to get length equal to NumOfItems
    while len(subset) < NumOfItems:
        subset = [0] + subset
    AllSubsets.append(subset)

print(AllSubsets)



data = [20, 10, 9, 4, 2, 1]
prices = {20:4000, 10:3500, 9:1800, 4:400, 2:1000, 1:200}
filteredSets = []
output = []


for set in AllSubsets:
    # print(">> For Set: ",set)
    sum = 0
    for idx in range(0,len(set)):
        if set[idx] == 1:
            sum = sum + data[idx]

    if sum == 20:
        print("----------------")
        print(">>",set)
        print(">> Sum is:",sum)
        print("----------------")
        print()
        filteredSets.append(set)

for set in filteredSets:
    sum = 0
    for idx in range(0, len(set)):
        if set[idx] == 1:
            sum = sum + prices[data[idx]]

    output.append(sum)

print(filteredSets)
print(output)



