# Code a function that takes one number a and multiplies it by 
# another number b and returns the product
def multiply(a,b):
    return a * b

# Code a function that finds the area of a 
# rectangle when given the width and length
def area(width,length):
    return width * length

# Code a function that takes one number a and divides it by 
# another number b and returns the quotient rounded up 
def division(a,b):
    if (a % b) == 0:
        return a//b
    return a//b + 1

#print(division(6,3))
#print(division(7,3))

#Write a for loop that prints the sum of all the numbers from 3 to 7
def loop():
    sum = 0
    for i in range(3,8):
        sum += i
    return sum
print(loop())
