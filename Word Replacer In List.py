wordToReplace = input("enter the word to find in the text")
replacingWord = input("enter the word to replace with")
lineNum = 0

text = open("beeScript.txt", "r+")
lineList = text.readlines()

for x in lineList:
    if wordToReplace in x:
        lineList[lineNum] = lineList[lineNum].replace(wordToReplace, replacingWord)
    lineNum+=1
text.truncate()
text.close()

text=open("beeScript.txt", "w+")
text.writelines(lineList)
text.close()


