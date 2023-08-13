from pprint import pprint as pp

flowerField = ["..........",
 "...FFFF...",
 "..FF.FFF..",
 "..F.F.F...",
 "..FF.FF...",
 "....F....."]

flowerFieldArray = [[character for character in row] for row in flowerField]

def plantFlowers(array):

    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == 'F':
                rowinc = -1
                if row == 0:
                    rowinc = 1
                colinc = -1
                if col == 0:
                    colinc = 1
                array[row + rowinc][col + colinc] = 'F'
                array[row + rowinc][col] = 'F'
                array[row][col + colinc] = 'F'
    
    return array

pp(flowerFieldArray)
pp(plantFlowers(flowerFieldArray))