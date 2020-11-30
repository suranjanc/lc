votesList=[str(item.strip()) for item in input('Please enter the votes: ').split(',')]

def calcMajority(listVotes):
    votesDict={}
    winner=''
    #print('The list and its length are: ', listVotes, ' & ',len(listVotes))
    for item in listVotes:
        if item in votesDict:
            votesDict[item]+=1
            if votesDict.get(item)>=len(listVotes)/2:
                winner=item
        else:
            votesDict[item]=1
    return winner

#main
print('The winner of the vote is: ', calcMajority(votesList))