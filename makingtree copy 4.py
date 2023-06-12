wordlist = ["pascal", "program", "programmer", "task", "tree",
 "treacherous", "treachery", "tread", "trace"]

class node:
    def __init__(self, letter):
        self.letter = letter
        self.children = []
    
    def display(self, level = 0):
        print(' '* level + self.letter)
        for c in self.children:
            c.display(level + 1)

class nodestate:
    def __init__(self, win, depth, str):
        self.win = win
        self.depth = depth
        self.str = str

"""node1 = node('f')
node2 = node1.children.append(node('i'))

node1.display()"""

tree = node('')

def maketree(parent, str):
    if len(str) == 0:
        return
    result = [ item for item in parent.children if item.letter == str[0]]
    if len(result) == 0:
        newNode = node(str[0])
        parent.children.append(newNode)
        maketree(newNode,str[1:])
    else: 
        maketree(result[0],str[1:])

wordlist.sort()    
for word in wordlist:
    if wordlist.index(word) == 0:
        maketree(tree,word)
    else:
        repeatwords = 0
        for prevwords in wordlist[:wordlist.index(word)]:
            if word.startswith(prevwords):
                repeatwords += 1
                break
        if repeatwords == 0:
            maketree(tree,word)

def winstate(selectednode, IsJoe = True):
    if len(selectednode.children) == 0:
        return nodestate(not IsJoe, 0, selectednode.letter)
    else:
        if IsJoe:
            states = [ winstate(item, not IsJoe) for item in selectednode.children]
            losingStates = [ item for item in states if item.win]
            if len(losingStates):
                losingState = sorted(losingStates, key=lambda item: item.depth, reverse=False)[0]
                return nodestate(True, losingState.depth +1, selectednode.letter + losingState.str )
            else:
                winningStates = [ item for item in states if not item.win]
                winS = sorted(winningStates, key=lambda item: item.depth, reverse=True)[0]
                return nodestate(False, winS.depth + 1, selectednode.letter + winS.str)
        else:
            states = [ winstate(item, not IsJoe) for item in selectednode.children]
            losingStates = [ item for item in states if not item.win]
            if len(losingStates):
                losingState = sorted(losingStates, key=lambda item: item.depth, reverse=False)[0]
                return nodestate(False, losingState.depth + 1, selectednode.letter + losingState.str )
            else:
                winningStates = [ item for item in states if item.win]
                winS = sorted(winningStates, key=lambda item: item.depth, reverse=True)[0]
                return nodestate(True, winS.depth + 1, selectednode.letter + winS.str)

tree.display()

print(winstate(tree).str)