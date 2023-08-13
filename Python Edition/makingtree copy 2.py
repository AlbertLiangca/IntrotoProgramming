wordlist = ['fire', 'fir', 'four']

class node:
    def __init__(self, letter):
        self.letter = letter
        self.children = []

    def __eq__(self, __value: object) -> bool:
        return __value == self.letter

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
    
    if not str[0] in parent.children:
        newNode = node(str[0])
        parent.children.append(newNode)
        maketree(newNode,str[1:])
    else: 
        result = [ item for item in parent.children if item.letter == str[0]]
        maketree(result[0],str[1:])
    
for word in wordlist:
    maketree(tree,word)
tree.display()