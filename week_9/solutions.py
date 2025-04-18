"Problem 1: Compute the factorial of a number"
def factorial(n:int)->int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


"Problem 2: Compute the sum of all the digits in a number"
def sum_of_digits(n:int)->int:
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


"Problem 3: Determine if the string is a palindrome"
def is_palindrome(s:str)->bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


"Problem 4: Determine the nth fibonacci number"
def fibonacci(n:int):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


"Problem 5: Determine if all of the numbers in a list sum up to an integer x"
def sum_to_x(l:list[int],x:int)->bool:
    if len(l) == 1:
        return l[0] == x
    return sum_to_x(l[1:],x-l[0])


"Problem 6: Determine if any mice appear in the nest"
DUST = "d"
MOUSE = "m"
def has_mice(nest) -> bool:
    if isinstance(nest, list):
        for e in nest:
            if has_mice(e):
                return True
        return False
    else:
        return nest == MOUSE


"Bonus Problem 1: Find the sum of a list recursively"
def sum_list(lst:list[int]) -> int:
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum_list(lst[1:])


"Bonus Problem 2: Reverse a list recursively"
def reverse_list(lst:list[int]) -> list[int]:
    if len(lst) == 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])


"Bonus Problem 3 (non recursion): Sum all of the values in a dictionary"
def sum_values(d:dict) -> int:
    num = 0
    for key in d.keys():
        num += d[key]
    return num
        


