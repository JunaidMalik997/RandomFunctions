def compareNum(numList, num):
    for number in numList:
        if (num == number):
            return True
    return False

boolResult = compareNum([1,2,4,6,7], 7)