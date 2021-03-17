limit = int(input("enter the highest number you want to find multiples up to"))
difference = int(input("enter the difference between multiples"))

def multiples(limit, difference):
    diff_list = []
    diff_const = difference
    for x in range (0, (int(limit/difference))):
        diff_list.append(difference)
        difference = difference + diff_const#without diff_const then difference doubles every time instead of adding the original difference input.
        print(diff_list)




multiples(limit,difference)








