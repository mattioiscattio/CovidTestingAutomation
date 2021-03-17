limit = int(input("enter the highest number you want to find multiples up to"))
difference = int(input("enter the difference between multiples"))

def multiples(limit, difference):
    diff = limit/difference
    diff = limit/diff
    diff_list = []
    for x in range (0, (int(limit/difference))):
        diff_list.append(diff)
        diff = diff + difference
        print(diff_list)




multiples(limit,difference)

