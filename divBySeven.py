def divByNos():
    listOfNos=[]
    for i in range(2000,3201):
        if (i%7==0) and (i%5!=0):
            listOfNos.append(str(i))
    return listOfNos

listNos=divByNos()
print(','.join(listNos))