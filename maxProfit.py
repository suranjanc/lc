priceList=[int(item) for item in input('Enter the list of numbers: ').strip().split(',')]

def maxProfit(priceList):
        profit=0
        for i in range(len(priceList)-1):
            if priceList[i+1] > priceList[i]:
                profit+=priceList[i+1]-priceList[i]
        return profit

#main
print(maxProfit(priceList))