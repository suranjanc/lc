inputList=[1,0,2,3,0,4,5,0]

def shiftRight(inputList):
    newlist=[]
    for i in inputList:
        newlist.append(i)
        if i==0:
            newlist.append(0)
    return newlist[0:len(inputList)]

print(shiftRight(inputList))