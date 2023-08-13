wordlist = ['fire', 'four']

class node:
    def __init__(self, letter):
        self.letter = letter
        self.children = []
    
    def display(self, level = 0):
        print(' '* level + self.letter)
        for c in self.children:
            c.display(level + 1)

"""node1 = node('f')
node2 = node1.children.append(node('i'))

node1.display()"""

tree = node('')

def maketree(parent, str):
    if len(str) == 0:
        return
    result = [d.letter for d in parent.children]
    print(result)
    if len(result) == 0:
        newNode = node(str[0])
        parent.children.append(newNode)
        maketree(newNode,str[1:])
    else: 
        maketree(result[0],str[1:])
    
for word in wordlist:
    maketree(tree,word)
tree.display()