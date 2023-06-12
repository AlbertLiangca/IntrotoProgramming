a = 147
b = 8
p = 3

def pickApples():
    pickedapples = [1]
    for i in range(1,b):
        if i <= p:
            x = 0
        else:
            x = pickedapples[i-(p+1)]
        pickedapples.append(pickedapples[i-1]*2 - x)
    """ if pickedapples[-1] > a:
        return []
    else:
        return pickedapples"""
    return pickedapples

print(pickApples())

# bin 1 2 3 4
# O(B*P)  time 
# O(B)    time 

#     1 2 4 
#     what b[i]?  starting 1 ... 
#       sum([i-p] ... [i-1])

#       p = 4, i = 1  , sum()+1 = 1
#      b[1-4] => b[-3]
#      b[1-3] => b[-2]
#      b[1-2] => b[-1]
#      b[1-1] => b[-0]
#      
#       p = 4, i = 2 , sum(p)+1 = 2
#      b[2-4] => b[-2]
#      b[2-3] => b[-1]
#      b[2-2] => b[-0]
#      b[2-1] => b[1]   1 

#       p = 4, i = 3 , sum(p)+1 = 4
#      b[3-4] => b[-1]
#      b[3-3] => b[-0]
#      b[3-2] => b[1]   1
#      b[3-1] => b[2]   2 
#      
