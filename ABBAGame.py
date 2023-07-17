initial = 'AAABBAABB'

target = 'BAABAAABAABAABBBAAAAAABBAABBBBBBBABB'

class node:
    def __init__(self, word):
        self.word = word
        self.children = []
        self.winstate = ''
    
    def display(self, level = 0):
        print(' '* level + self.word)
        for c in self.children:
            c.display(level + 1)

gametree = node(initial)

def ABBAGameTree(parent, target):
    if len(parent.word) == len(target):
        return parent
    
    else:
        parent.children.append(node(parent.word+'A'))
        reverseb = parent.word + 'B'
        parent.children.append(node(reverseb[::-1]))
        for item in parent.children:
            ABBAGameTree(item, target)

ABBAGameTree(gametree, target)

winstate = 'impossible'

def WalkTree(parent):
    
    global winstate

    if len(parent.children) == 0:
        if parent.word == target:
            winstate = 'possible'
    
    else:
        for item in parent.children:
            WalkTree(item)
    
    return winstate

WalkTree(gametree)