import time
text = open("text.txt")
text.seek(0)
lines = text.read().splitlines()
text.close()
for x in range(len(lines)):
    lines[x] = lines[x].split(" ")
    for y in range(len(lines[x])):
        if lines[x][y] == "the":
            lines[x][y] = "test"
        lines[x][y] += ("\n")
print(lines)
text =  open("text.txt", "r")
x=0
for line in text:
    text.write(lines[x])
    print(lines[x])
    x+=1
text.close()