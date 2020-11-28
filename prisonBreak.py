#input the cell 
inputList=[int(item) for item in input('Enter the prison list in 0s and 1s: ').strip().split(',')]

#def to release prisoners
def relPrisoners(passedList):
    if passedList[0]==0:
        return(0)
    countFreed=0
    newlist=passedList.copy()
    for i in range(len(passedList)):
        if newlist[i]==1:
            countFreed+=1
            newlist=listToggle(newlist)
    return(countFreed)

def listToggle(listName):
    toggledList=[]
    for i in range(len(listName)):
        if listName[i]==0:
            toggledList.append(1)
        else:
            toggledList.append(0)
    return(toggledList)

#main to call def
print(relPrisoners(inputList))