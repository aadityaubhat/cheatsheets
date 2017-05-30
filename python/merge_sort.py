def merge_sort(numberList):
    if len(numberList) > 1:
        mid = len(numberList) / 2
        left = numberList[0:mid]
        right = numberList[mid:]

        merge_sort(left)
        merge_sort(right)

        l, r = 0, 0

        for ind in xrange(0, len(numberList)):

            lval = left[l] if l < len(left) else None
            rval = right[r] if r < len(right) else None

            if (lval != None and rval != None and lval < rval) or rval is None:
                numberList[ind] = lval
                l += 1
            elif (lval != None and rval != None and lval >= rval) or lval is None:
                numberList[ind] = rval
                r += 1

a = [5,4,1,3,5,8, 0]

merge_sort(a)

print(a)