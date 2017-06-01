import random,time

def partition(numberList, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if numberList[i] <= numberList[begin]:
            pivot += 1
            numberList[i], numberList[pivot] = numberList[pivot], numberList[i]
    numberList[pivot], numberList[begin] = numberList[begin], numberList[pivot]
    return pivot



def quick_sort(numberList, begin=0, end=None):
    if end is None:
        end = len(numberList) - 1
    def _quicksort(numberList, begin, end):
        if begin >= end:
            return
        pivot = partition(numberList, begin, end)
        _quicksort(numberList, begin, pivot-1)
        _quicksort(numberList, pivot+1, end)
    return _quicksort(numberList, begin, end)

randomNumberList = random.sample(xrange(-1000000000, 1000000000), 10000)

start_time = time.time()
quick_sort(randomNumberList)
print("--- %s seconds ---" % (time.time() - start_time)) # 0.0317330360413

print(randomNumberList == sorted(randomNumberList))