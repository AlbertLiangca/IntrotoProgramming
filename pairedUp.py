lo = 1234
hi = 654321

def allEven():
    pairedup = []
    for i in range(lo,hi):
        numberaslist = []
        for digit in str(i):
            numberaslist.append(digit)
        odddigits = 0
        for num in range(10):
            x = str(num)
            if numberaslist.count(x) % 2 != 0:
                odddigits += 1
        if odddigits == 0:
            pairedup.append(i)
    return len(pairedup)

print(allEven())