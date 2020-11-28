inputList=[int(item) for item in input('Enter the list items: ').strip().split(',')]

for item in inputList:
    if item==0:
        inputList.remove(item)
        inputList.append(item)

print(inputList)