#Imports And Var's
import tkinter as tk

#Classes and Functions
class covidTest():#add gui/text interface to select options from class (tkinter)
    def fileStructure(self, yearGroups, formTitles):
        lineNum = 1
        covidTest().dataStorageClear()#wipes the data file, use carefully
        dataFile = open("covidTestData.txt", "a")
        for i in yearGroups:
            dataFile.write(str(i)+" :This is the year group \n")
        dataFile.close()

        dataFile = open("covidTestData.txt", "r")
        dataVar = dataFile.readlines()
        dataVarTemp = list(dataVar)
        dataFile.close()

        for line in dataVarTemp:
            if line[-12:-2] == "year group":
                for formName in formTitles:
                    dataVar.insert(lineNum, "    "+formName+" :This is the form name\n")
                    lineNum+=1
                lineNum+=1
        dataVar.append("Infected Students:\n")
        dataVar.insert(0,"Student Data In Format: Year Group:Form Group:Days Since Last Test:Name \n")
        covidTest().dataStorageClear()
        dataFile = open("covidTestData.txt", "w")
        dataFile.writelines(dataVar)
        dataFile.close()

    def studentAdder(self, studentName, studentYearGroup, studentForm):#adds students to the data structure, live database, maybe make backup system? have list /ability to select between years and forms rather than just have to type them in. Maybe have title of type in datafile, ie year=8, form=E, name=test, to allow for location of info dynamically, ie find "name" in line then after that is the actual name
        studentYearGroup = str(studentYearGroup)
        dataFile = open("covidTestData.txt", "r")
        data = dataFile.readlines()
        dataFile.close()
        yearGroup = False
        for line in range(len(data)):
            if data[line][0:1] == studentYearGroup or data[line][0:2] == studentYearGroup:
                yearGroup = True
            if data[line][4:5] == studentForm and yearGroup == True:
                data.insert(line+1,"            "+ studentYearGroup+":"+studentForm+":0:False:"+studentName+"\n")
                covidTest().dataStorageClear()
                dataFile = open("covidTestData.txt", "w")
                for line in data:
                    dataFile.write(line)
                dataFile.close()
                break

    def studentDataSearch(self, studentSearch, studentSearchResult):
        found = False
        dataFile = open("covidTestData.txt", "r")
        data = dataFile.readlines()
        for line in reversed(data):#find reason that this opens apparently in reverse? maybe the search algorithm.
            if studentSearch.upper() in line.upper() and line[0] == " " and line[4] == " ":
                studentSearchResult.configure(text=line, font=("Courier", 9))#add text resizing algorithm using len(line) and maths
                found = True
        if found == False:
            studentSearchResult.configure(text="data not found in database")
        dataFile.close()



    def dataStorageClear(self):#wipes the data file, use carefully, add authentication/assurance in future
        dataFile = open("covidTestData.txt", "w")
        dataFile.truncate()
        dataFile.close()

    def start(self):
        yearGroups=[7,8,9,10,11]
        formTitles = ["P", "E", "N", "A", "I", "R", "S", "C"]
        window = tk.Tk()#initiliases window
        window.geometry("600x700")
        window.title("Covid Test Automation")

        studentNameText = tk.Label(window, text="Enter Student Name Here ->", fg="white", bg="red", font=("Courier", 13)).place(height=50, width=300, x=0, y=0)
        studentName = tk.Entry(window, fg="white", bg="red", font=("Courier", 15))  # .place must be seperate from initial assign for .get to work.
        studentName.place(height=50, width=300, x=300, y=0)  # use of lambda is necessary for command, just using a function runs it on startup, not just on click, breaks anything using it.

        studentYearGroupText = tk.Label(window, text="Enter Stduent Year Group Here\/", fg="white", bg="red", font=("Courier", 11)).place(height=50, width=300, x=0, y=50)
        studentYearGroup = tk.Listbox(window, exportselection=0, fg="white", bg="red", font=("Courier", 15))
        for i in yearGroups:
            studentYearGroup.insert(yearGroups.index(i), i)
        studentYearGroup.place(height=200, width=300, x=0, y=100)

        studentFormText = tk.Label(window, text="\/Enter Student Form Group Here", fg="white", bg="red", font=("Courier", 11)).place(height=50, width=300, x=300, y=50)
        studentForm = tk.Listbox(window, exportselection=0,  fg="white", bg="red", font=("Courier", 15))
        for i in formTitles:
            studentForm.insert(formTitles.index(i), i)
        studentForm.place(height=200, width=300, x=300, y=100)

        studentSearchText = tk.Label(window, text="Enter Student To Search ->", fg="white", bg="red", font=("Courier", 13)).place(height=50, width=350, x=0, y=350)
        studentSearch = tk.Entry(window, fg="white", bg="red", font=("Courier", 15))
        studentSearch.place(height=50, width=200, x=350, y=350)
        studentSearchStart = tk.Button(window, text="Search", fg="white", bg="red", font=("Courier", 10), command=lambda: covidTest().studentDataSearch(studentSearch.get(), studentSearchResult)).place(height=50, width=50, x=550, y=350)#show this in a "console" in gui
        studentSearchResult = tk.Label(window, text=". . .", fg="white", bg="red", font=("Courier", 10))
        studentSearchResult.place(height=50, width=600, x=0, y=400)

        #timeText = tk.Label(window, text=)
        #timeIncrease

        dataInput = tk.Button(window, text="input data", fg="white", bg="red", font=("Courier", 15), command=lambda: covidTest().studentInput(studentName, studentYearGroup, studentForm, yearGroups, formTitles)).place(height=50, width=600, x=0, y=300)
        resetData = tk.Button(window, text="Reset All Data", fg="white", bg="red", font=("Courier", 15), command=lambda: covidTest().fileStructure(yearGroups, formTitles)).place(height=50, width=600, x=0, y=650)

        window.mainloop()

    def studentInput(self, studentName, studentYearGroup, studentForm, yearGroups, formTitles):
        covidTest().studentAdder(studentName.get(), yearGroups[studentYearGroup.curselection()[0]], formTitles[studentForm.curselection()[0]])
        studentName.delete(0, "end")

    def timePassage(self):#have button to incrase/decrease time to real time, then apply time update
        dataFile = open("covidTestData.txt", "r")
        data = dataFile.readlines()
        for line in data:
            if line[0] == " " and line[4] == " ":#shows that there is no header for yeargroup/other on that line, ie shows its a student data line
                print(line)#edit days since last test
                print(line.split(":"))



covidTest().start()#starts the program.




