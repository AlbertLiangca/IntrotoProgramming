encodedword = 'huffman'

class node:
    def __init__(self, letter, freq):
        self.freq = freq
        self.letter = letter
        self.children = []

    def display(self, level = 0):
        print(' '* level + self.letter)
        for c in self.children:
            c.display(level + 1)

def HuffmanTreemaker(word):
    wordaslist = []
    letterswithweights = {}

    for letter in word:
        wordaslist.append(letter)

    for letter in wordaslist:
        letterswithweights[letter] = wordaslist.count(letter)
    
    sortedletterswithweights = sorted(letterswithweights.items(),key = lambda x:x[1])
    nodes = [node(item[0], item[1]) for item in sortedletterswithweights]

    while len(nodes) > 1:
        y = node(nodes[0].letter+ nodes[1].letter, nodes[0].freq + nodes[1].freq)
        y.children.extend([nodes[0], nodes[1]])
        del nodes[0]
        del nodes[0]
        nodes.append(y)
        nodes.sort(key = lambda x: (x.freq, -len(x.letter)))
    
    fulltree = nodes[0]
    fulltree.display()
    return fulltree

lettertobinary = {}

def HuffmanEncoder(parent, binarycode = ''):

    if len(parent.children) == 0:
        lettertobinary[parent.letter] = binarycode
    else:
        HuffmanEncoder(parent.children[0], binarycode + '0')
        HuffmanEncoder(parent.children[1], binarycode + '1')


binarytree = HuffmanTreemaker(encodedword)

HuffmanEncoder(binarytree)

print(lettertobinary)

huffmanword = ''

for letter in encodedword:
    huffmanword += lettertobinary[letter]

print(huffmanword)

print(len(huffmanword))
