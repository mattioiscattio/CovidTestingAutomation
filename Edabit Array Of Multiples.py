num = int(input("enter the number to multiply"))
length = int(input("how many multiples to create"))
multipleArray = []
x=1

def lastUpdatePos():
    arrayFile = open("multipleArray.txt", "r")
    enumeratedFile = (list(enumerate(arrayFile.readlines())))  #prints the readlines function enumerated, giving the line number of each item in the file as a list of tuples, format = linenum, item.
    for i in reversed(enumeratedFile):#uses reversed to loop through the list in reverse, this can improve efficiency.
        if "run" in i[1]:#checks for run in the enumerated list
            lineOfLastUpdate = (i[1].split(" "))[9]
            break
    arrayFile.close()
    return lineOfLastUpdate

while len(multipleArray) < length:
    multipleArray.append(num*x)
    x+=1
print(multipleArray)

arrayFile = open("multipleArray.txt", "a")#using a instead of w/other alternatives as the file access method, this allows to add to the end of a file as a log, rather than just overwriting every time.
arrayFile.write("multipleArray run with num="+str(num)+" and length="+str(length)+" this is run "+str(int(lastUpdatePos())+1)+" of the program\n")#writes the config/information line with the previous config lines run num+1
for i in multipleArray:
    arrayFile.write(str(i)+"\n")#loops through the multipleArray list and adds each number on its own line

arrayFile.close()






