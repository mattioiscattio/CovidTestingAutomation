def messages():
    message = str(input("enter the message"))
    flashes = int(input("enter the number of flashes"))

    while not len(message) <= 20:
        message = str(input("enter the message"))
    for x in range(flashes):
        print(message)

def studentdatachallenge():
    studentdata = [["Kirstie", False], ["James", True]]
    student_name = str(input("enter the name of the student you watn to find"))
    if any(student_name in subl for subl in studentdata):
        print(studentdata[studentdata.index(student_name)])
    else:
        print("no")
def listiteration():
    # Python3 code to iterate over a list
    list = [[1, 3, 5, 7, 9]]

    # Using list comprehension
    [print(i) for i in list]





mode = str(input("enter message/studentdatachallenge/listiteration"))
#while mode.lower() == "studentdatachallenge" or "messages" or "listiteration":
    #print("type better nub")
    #mode = input("enter message/studentdatachallenge/listiteration")

if mode.lower() == "message":
    messages()
elif mode.lower() == "studentdatachallenge":
    studentdatachallenge()
elif mode.lower() == "listiteration":
    listiteration()






