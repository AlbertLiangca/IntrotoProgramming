def addReverse(string):
    for i in range(int(string)):
        rev = []
        revasstring = ''
        for j in str(i):
            rev.append(j)
        rev.reverse()
        for item in rev:
            revasstring += item
        revnum = int(revasstring)
        total = revnum + i
        if str(total) == string:
            return str(i)
        
print(addReverse('88'))