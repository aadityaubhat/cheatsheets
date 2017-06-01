import random, time

def insertion_sort(numberList):
    for ind in xrange(0, len(numberList)):
        currentInd = ind

        while currentInd > 0 and numberList[currentInd] < numberList[currentInd - 1]:
            numberList[currentInd], numberList[currentInd - 1] =numberList[currentInd - 1], numberList[currentInd]
            currentInd -= 1


randomNumberList = random.sample(xrange(-1000000000, 1000000000), 10000)

start_time = time.time()
insertion_sort(randomNumberList)
print("--- %s seconds ---" % (time.time() - start_time)) # 5.35385990143

print( randomNumberList == sorted(randomNumberList))