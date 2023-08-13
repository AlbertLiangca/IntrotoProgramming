def FizzBuzz(number):
    
    for i in range(number + 1):
        print('Fizz'*(i%3<1) + 'Buzz'*(i%5<1) or i)

array = [1]
print(array[-1])