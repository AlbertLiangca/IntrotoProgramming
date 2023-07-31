initial = 'BAAAAABAA'

target = 'BAABAAAAAB'

winstate = 'impossible'

def ABBAGameTree(initial, target):
    
    global winstate
    
    if len(initial) == len(target):
        if initial == target:
            winstate = 'possible'
            return winstate
    
    else:
        if target[-1] == 'A':
            ABBAGameTree(initial, target[:-1])
        if target[0] == 'B':
            reverseb = target[1:]
            ABBAGameTree(initial, reverseb[::-1])
    
    return winstate

print(ABBAGameTree(initial, target))

