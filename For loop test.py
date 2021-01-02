"""num = int(input("enter the binary number"))
for x in range(len(str(num))):
    ans = (str(num)[x])
    print(x)
    """
binary = input("Input a number in binary:")
denary = 0
for digit in binary:
    print(digit)
    denary = denary * 2 + int(digit)
print("Your denary number is: " , denary)