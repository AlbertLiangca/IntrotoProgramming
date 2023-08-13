teststreet = [3,7,8,3,6,1]

def dadSunsetSol(street):
    sunsetbdings = [float('inf')]
    for building in street:
        while building >= sunsetbdings[-1]:
            sunsetbdings.pop()
        sunsetbdings.append(building)
    return len(sunsetbdings[1:])

print(dadSunsetSol(teststreet))

def AlbertSunsetSol(street):
    sunsetbdings = []
    for building in street:
        sunsetbdings.append([])
        sunsetbdings[-1].append(building)
        for view in sunsetbdings[:-1]:
            if building > view[0]:
                sunsetbdings.remove(view)
    return len(sunsetbdings)

print(AlbertSunsetSol(teststreet))
            