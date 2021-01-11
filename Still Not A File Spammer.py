
def open_file():
    timer = 0
    test = 1
    for x in range(5000):
        file = open(str(test) + ".txt", "w+")
        for i in range(2000):
            file.write("have some files and less storage %d\r\n" % (i + 1))
        file.close()
        test+=1


open_file()