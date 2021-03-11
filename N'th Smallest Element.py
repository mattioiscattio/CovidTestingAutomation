num_list = []
iterations = int(input("enter the amount of numbers you want on your list"))
element = int(input("enter the location of the digit that you want to find in the sorted list of numbers"))
for x in range(0, iterations):
    nums = int(input("enter the number you want to add to your list"))
    num_list.append(nums)
    print(num_list)

num_list.sort()
print(num_list)
print(num_list[element-1])
















































