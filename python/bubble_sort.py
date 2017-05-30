import random

def bubble_sort(numberList):
    """
    Sorts a list of unsorted numbers using Bubble Sort algorithm

    :param numberList: A list of unsorted numbers
    :return: A list of sorted numbers in an Ascending order
    """
    swap = True
    while swap:
        swap = False
        for ind in xrange(0,len(numberList)):
            if ind + 1 < len(numberList):
                if(numberList[ind] > numberList[ind + 1]):
                    numberList[ind], numberList[ind + 1] = numberList[ind + 1], numberList[ind]
                    swap = True

    return numberList


randomNumberList = random.sample(xrange(-1000000000, 1000000000), 10000)

print(bubble_sort(randomNumberList) == sorted(randomNumberList))

