inputList=[int(item) for item in input('Please enter the list: ').split(',')]
#print(inputList)

def diffList(passedList):
    #uniqueList=list(set(passedList))
    leftOnes=[]
    for item in passedList:
        if passedList.count(item) ==1:
            leftOnes.append(item)
    print(leftOnes)

#main
diffList(inputList)



