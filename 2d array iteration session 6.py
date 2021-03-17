list = [[1,2,3,4,5,6],[11,12,13,14,15,16,],[21,22,23,24,25, 26],[31,32,33,34,35, 36]]
totalValue = 0
for arrayNum in range(len(list)):
    for value in list[arrayNum]:
        totalValue = totalValue + value
    print(totalValue/len(list[arrayNum]), "this is the mean of row", arrayNum)
    totalValue = 0
    arrayNum += 1
