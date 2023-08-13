longx = 500000
longy = 500000

def VariableRange(list1, list2):
    if len(list1) == 0:
        return range(len(list2))
    else:
        return range(list2.index(list1[-1]))

def findMinimumValue(longx, longy):
    total = longx + longy
    pointsperturn = []
    i = 1
    while sum(pointsperturn) < total:
        pointsperturn.append(2*i-1)
        i += 1
    
    if sum(pointsperturn) > total:
        return -1

    Alicewinningturns = []

    while longx - sum(Alicewinningturns) != 0:
        nextlargestnum = 0    
        for x in VariableRange(Alicewinningturns, pointsperturn):
            if pointsperturn[x] > nextlargestnum and pointsperturn[x] + sum(Alicewinningturns) <= longx and longx - pointsperturn[x] != 2 and pointsperturn[x] not in Alicewinningturns:
                nextlargestnum = pointsperturn[x]
        Alicewinningturns.append(nextlargestnum)

    return len(Alicewinningturns)


print(findMinimumValue(longx, longy))
    