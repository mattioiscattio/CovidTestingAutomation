def testFunction(testList, testVar):
    if testVar == "x":
        testList.append(testVar)
    elif testVar == "y":
        testList = []


    print(testList)
    return  testList

testList = []
while True:
    testVar = input("enter input brrr")
    testList = testFunction(testList, testVar)