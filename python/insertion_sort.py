import random

def insertion_sort(numberList):
    for ind in xrange(0, len(numberList)):
        currentInd = ind

        while currentInd > 0 and numberList[currentInd] < numberList[currentInd - 1]:
            numberList[currentInd], numberList[currentInd - 1] =numberList[currentInd - 1], numberList[currentInd]
            currentInd -= 1

    return numberList


randomNumberList = random.sample(xrange(-1000000000, 1000000000), 10000)

print insertion_sort([2,4,6,90,1,45,23,7, 0, -1])

print(insertion_sort(randomNumberList) == sorted(randomNumberList))
