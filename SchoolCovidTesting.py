#Imports And Var's

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

        covidTest().dataStorageClear()
        dataFile = open("covidTestData.txt", "w")
        dataFile.writelines(dataVar)
        dataFile.close()

    def dataStorageClear(self):#wipes the data file, use carefully, add authentication/assurance in future
        dataFile = open("covidTestData.txt", "w")
        dataFile.truncate()
        dataFile.close()

#Main Code
covidTest().fileStructure(yearGroups=[7,8,9,10,11], formTitles=["P", "E", "N", "A", "I", "R", "S", "C"])#add creation of these list per user basis
