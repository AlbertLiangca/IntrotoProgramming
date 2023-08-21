import time

def FizzBuzz(number):
    return (('Fizz'*(i%3<1) + 'Buzz'*(i%5<1) or i) for i in range(number + 1))

def pickHighestNum(array):
    
    currentHighest = 0
    for i in array:
        if i > currentHighest:
            i = currentHighest
    
    return currentHighest
