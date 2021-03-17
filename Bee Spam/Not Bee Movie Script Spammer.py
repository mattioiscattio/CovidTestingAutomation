Bee = open("Bee.txt", "r")
text = Bee.read()
spam = 1
for x in range(50):
    f = open(str(spam) +".txt", "w+")
    f.write(text)
    f.close()
    spam+=1


























































