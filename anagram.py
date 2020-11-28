anagramList=[str(item).strip() for item in input('Enter the anagram list: ').split(',')]
print(anagramList)#: eat, tea, tan, ate, nat, bat

#This def sorts the list of each word and adds to a new listed as a sorted word 
def clubAnagrams(anagramList):
    sortedAnagams=[]
    for i in range(len(anagramList)):
        sortedItem=''.join(sorted(anagramList[i]))
        sortedAnagams.append(sortedItem)
    print(sortedAnagams)
    return sortedAnagams

def putIntoSubList(passedList):
    finalList=[]
    final2=[]
    for i in range(len(passedList)):
        if not any(passedList[i] in subList for subList in finalList):
            finalList.append([passedList[i]])
            final2.append([anagramList[i]])
        else:
            #find the index of the sublist where this i exists
            indexPosition=searchIndexPosition(finalList, passedList[i])
            finalList[indexPosition].append(passedList[i])
            final2[indexPosition].append(anagramList[i])
    return final2

def searchIndexPosition(listToSearch, itemToSearch):
    for subList in listToSearch:
        for item in subList:
            if item==itemToSearch:
                indexfound = listToSearch.index(subList)
    return indexfound

#main
newList=clubAnagrams(anagramList)
print(putIntoSubList(newList))