candidateList = []
highestVote = []

def candidateinput(candidateList):
    candidateNum = int(input("enter the number of candidates"))
    for i in range(candidateNum):#this section creates the list of candidates and gathers information about them.
        candidateName = input("enter the candidate name")
        candidateAge = int(input("enter the candidate age in years, candidates must be between 25 and 100"))
        while candidateAge >100 and candidateAge < 25:
            candidateAge = int(input("enter the candidate age in years"))
        candidateInfo = input("enter info about the candidate")
        candidateList.append([candidateName, candidateAge, candidateInfo, 0])

def voteChecks(candidateList, voteFound, vote):#checks if the vote is available, if not asks for a new vote and repeats.
    voteFound = False
    vote = input("enter one of the candidates names to vote for them.")
    for j in candidateList:
        if vote == j[0]:
            voteFound = True
            candidateList[candidateList.index(j)][3] = int(candidateList[candidateList.index(j)][3]) + 1
            break
        else:
            pass
    if voteFound == False:
        print("vote not found")
        vote = input("enter one of the candidates names to vote for them.")
        voteChecks(candidateList, voteFound, vote)

def voteCount(candidateList, highestVote):#finds the highest vote/s in the list of candidates and prints it.
    for i in candidateList:
        if 1 > len(highestVote):
            highestVote.append(i)
        elif i[1] > highestVote[0][3]:
            if 1 < len(highestVote):
                highestVote.clear()
                highestVote.append(i)
            else:
                highestVote[0] = i
        elif i[1] == highestVote[0][3]:
            highestVote.append(i)
    return highestVote

candidateinput(candidateList)
print(candidateList, "this is the list of candidates and info about them.")#gathers votes and adds them to the candidates values.
userNum = int(input("enter how many people are voting now."))
for i in range(userNum):
    voteChecks(candidateList, voteFound, vote)
print(voteCount(candidateList, highestVote), "this is the final winner and information about them in order, name, age, extra info, votes.\n", "all the candidates and their information/vote count shown below.\n", candidateList)
