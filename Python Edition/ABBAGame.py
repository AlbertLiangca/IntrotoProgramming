initial = 'AAABAAABB'

target = 'BAABAAABAABAABBBAAAAAABBAABBBBBBBABB'

def ABBAGameTree(initial, target):
    if len(initial) == len(target):
        return initial == target
    
    if target[-1] == 'A':
        if ABBAGameTree(initial, target[:-1]):
            return True
        
    if target[0] == 'B':
        reverseb = target[1:]
        return ABBAGameTree(initial, reverseb[::-1])
    else:
        return False

print(ABBAGameTree(initial, target))

