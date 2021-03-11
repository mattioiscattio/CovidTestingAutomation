import os.path
import time
start = time.time()
def open_file():
    timer = 0
    test = 1
    for x in range(1000):
        file = open((os.path.join("C:", str(test) + ".txt")), "w+")
        for i in range(200):
            file.write("have some files and less storage %d\r\n" % (i + 1))
        file.close()
        test+=1
open_file()
end=time.time()
print(end-start)































