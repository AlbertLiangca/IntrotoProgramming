import math

a = '685.4(757)'
b = '45.356(43)'

def addPeriodical(a,b):

    axy, az = a.split('(')
    ax, ay = axy.split('.')
    az = az[:-1]

    bxy, bz = b.split('(')
    bx, by = bxy.split('.')
    bz = bz[:-1]

    if len(ay) >= len(by):
        biggesty = ay

    else:
        biggesty = by

    while len(axy[axy.index('.'):]) < len(az) * len(bz) + len(biggesty):
        axy += az

    while len(bxy[bxy.index('.'):]) < len(az) * len(bz) + len(biggesty):
        bxy += bz  

    c = float(axy) + float(bxy)
    cstr = str(c)
    cstrdi = cstr.index('.')
    cstrz = cstr[(cstrdi + int(len(biggesty))+1):]
    cstrxy = cstr[:(cstrdi + int(len(biggesty))+1)]
    cstrx, cstry = cstrxy.split('.')
    for i in range(len(cstrz)):
        if len(cstrz) % (i + 1) == 0:
            if i == 0:
                potcstrz = cstrz[0]
            else:
                pocstrz = cstrz[:i]

            if potcstrz * int((len(cstrz) / (i+1))) == cstrz:
                cstrz = potcstrz
                break
    
    while cstry.endswith(cstrz):
        cstry = cstry[:-(len(cstrz))]

    if cstrz == '9':
        newc = cstrx + '.' + cstry + cstrz
        roundedc = round(float(newc),len(newc[newc.index('.')+1:])-1)
        roundedc = str(roundedc)
        finalc = roundedc[:-1] + '(' + roundedc[-1] + ')'
    else:
        finalc = cstrx + '.' + cstry + '(' + cstrz + ')'


    return finalc


print(addPeriodical(a,b))





