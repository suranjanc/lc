inputNos=str(input('Enter the number: ').strip())

def checkIfHappy(inputNos):
    isHappy=False
    while isHappy==False:
        newNos=0
        for i in inputNos:
            newNos+=int(i)**2
        if newNos==1:
            isHappy=True
        else:
            inputNos=str(newNos)
    return isHappy

print(checkIfHappy(inputNos))