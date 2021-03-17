unSortedInput = list(input("enter the number that you want to sort"))
repeat = 1
loopNum = 0

def intSwap(num1, num2):
    num2 += num1
    num1 = num2 - num1
    num2 = num2 - num1
    unSortedInput[digit] = num1
    unSortedInput[digit+1] = num2
    return (unSortedInput)

while repeat == 1:
    repeat = 0
    loopNum += 1

    for digit in range(len(unSortedInput)-1):
        if int(unSortedInput[digit]) > int(unSortedInput[digit+1]):
            intSwap(int(unSortedInput[digit]), int(unSortedInput[digit+1]))
            repeat = 1
        else:
            print(loopNum, "this is the amount of iterations of the sorting algorithm")
print("sorting complete the result is ", unSortedInput)