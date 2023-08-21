teststreet = [3,7,8,3,6,1]

class Stack:
    def __init__(self):
        self.array = []

    
    def pop(self):
        del self.array[-1]
    
    def push(self, elem):
        self.array.append(elem)
    
    def top(self):
        return self.array[-1]
        
    def isEmpty(self):
        return not len(self.array)
    
def dadSunsetSol(street):
    sunsetbdings = Stack()
    for building in street:
        while not sunsetbdings.isEmpty() and sunsetbdings.top() < building:
            sunsetbdings.pop()
        sunsetbdings.push(building)
    return len(sunsetbdings.array)

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

