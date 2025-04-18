"Problem 1: Compute the factorial of a number"
def factorial(n:int)->int:
    return

# print(factorial(4))   # Output: 24
# print(factorial(5))   # Output: 120
# print(factorial(6))   # Output: 720


"Problem 2: Compute the sum of all the digits in a number"
def sum_of_digits(n:int)->int:
    return

# print(sum_of_digits(423))   # Output: 9
# print(sum_of_digits(52))   # Output: 7
# print(sum_of_digits(1493))   # Output: 17


"Problem 3: Determine if the string is a palindrome"
def is_palindrome(s:str)->bool:
    return

# print(is_palindrome("llol"))   # Output: False
# print(is_palindrome("tacocat"))   # Output: True
# print(is_palindrome("racecar"))   # Output: True


"Problem 4: Determine the nth fibonacci number"
def fibonacci(n:int):
    return

# print(fibonacci(5))   # Output: 5
# print(fibonacci(6))   # Output: 8
# print(fibonacci(8))   # Output: 21


"Problem 5: Determine if all of the numbers in a list sum up to an integer x"
def sum_to_x(l:list[int])->bool:
    return

#print(sum_to_x([5,7,1],13))   # Output: True
#print(sum_to_x([8,3,1,1,4],12))   # Output: False
#print(sum_to_x([10,3,7],20))   # Output: True


"Problem 6: Determine if any mice appear in the nest"
DUST = "d"
MOUSE = "m"
def has_mice(nest:list[list]) -> bool:
    return

# print(has_mice([[DUST], DUST, [MOUSE, DUST]])) # Output: True
# print(has_mice(([[DUST], DUST, [DUST, DUST]]))) # Output: False
# print(has_mice([MOUSE])) # Output: True


"Bonus Problem 1: Find the sum of a list recursively"
def sum_list(lst:list[int]) -> int:
    return

# print(sum_list([5,7,2]))   # Output: 14
# print(sum_list([8,3,1,2,4]))   # Output: 18
# print(sum_list([10,3]))   # Output: 13


"Bonus Problem 2: Reverse a list recursively"
def reverse_list(lst:list[int]) -> list[int]:
    return

# print(reverse_list([5,7,2]))   # Output: [2,7,5]
# print(reverse_list([8,3,1,2,4]))   # Output: [4,2,1,3,8]
# print(reverse_list([10,3]))   # Output: [3,10]


"Bonus Problem 3 (non recursion): Sum all of the values in a dictionary"
def sum_values(d:dict) -> int:
    return

#print(sum_values({"a":3, "b":2, "c":7}))   # Output: 12
#print(sum_values({"a":8, "b":-2, "c":4, "d":9}))   # Output: 19
#print(sum_values({"a":9, "b":1, "c":2, "d":1}))   # Output: 13