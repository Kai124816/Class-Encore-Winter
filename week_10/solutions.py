#1.
    #What does this program print?
def recursive_evaluation(num:int)->int:
    if num % 3 == 0:
        return num//3
    elif num % 2 == 0:
        return num//2
    else:
        return recursive_evaluation(max(num-3,0))

# print(recursive_evaluation(7))  #2
# print(recursive_evaluation(1))  #0
# print(recursive_evaluation(recursive_evaluation(9)))  #1


#2.
    #What does this program print?
def most_common_letter(word:str)->str:
    my_dict = {}
    most_common = None
    max_apperances = 0

    for char in word:
        if char in my_dict.keys():
            my_dict[char] += 1
        else:
            my_dict[char] = 1
        if my_dict[char] >= max_apperances:
                most_common = char
                max_apperances = my_dict[char]
    return most_common

# print(most_common_letter("helloworld")) #l
# print(most_common_letter("abcdefghijk")) #k


#3.
    #What does this program print?
def sum_of_list(l:list)->int:
    total = 0
    for i in range(len(l)-1):
        if isinstance(l[i],int):
            if l[i] % 2 == 0:
                total += l[i]
            elif l[i] % 2 == 1:
                total += l[i] - 1
        else:
            if l[i] == 'A' or l[i] == 'a':
                total += 2
            else:
                total -= 3
    return total

l1 = [1,4,5,'A',9,[],'a']
print(sum_of_list(l1))


#4.
    #Debug the following function
def contains_pairs(lst:list, target:int) -> bool:
    """
    Returns True if a pair of elements in the list combine to the target int
    Returns False otherwise
    
    Example:
    >>> contains_pairs([1, 2, 3, 4, 5, 6], 7)
    True
    >>> contains_pairs([1, 1, 2, 3, 4], 8)
    False
    >>> contains_pairs([], 10)
    False
    """
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == target: #check if elements have same index
                return True
    return False #unindent false statement


#5.
    #Debug the following function
def second_largest(numbers: list[int]) ->int:
    """
    Returns the second largest number in the list.
    """
    if len(numbers) < 2:
        return None  # Edge case: List must have at least two distinct elements

    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest  # Move the old largest to second place
            largest = num
        elif second_largest < num < largest:
            second_largest = num

    return second_largest


#6.
    #Finish the following function
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

print(has_mice([[DUST], DUST, [MOUSE, DUST]])) # Output: True
print(has_mice(([[DUST], DUST, [DUST, DUST]]))) # Output: False
print(has_mice([MOUSE])) # Output: True


#7.
    #Finish the following function
def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    From a list of (name, value) pairs, select the pairs with the smallest
    value for each name. >>> smallest_each([("apple", 13), ("orange", 12), ("apple", 7), ("orange", 22)])
    [('apple', 7), ('orange', 12)]
    """
    pair_dict = {}
    for el in li:
        if el[0] in pair_dict.keys() and el[1] < pair_dict[el[0]]:
            pair_dict[el[0]] = el[1]
        elif el[0] not in pair_dict.keys():
            pair_dict[el[0]] = el[1]
    
    final_list = []
    for key in pair_dict.keys():
        final_list.append((key,pair_dict[key]))
    
    return final_list

print(smallest_each([("apple", 13), ("orange", 12), ("apple", 7), ("orange", 22)])) #[('apple', 7), ('orange', 12)]
print(smallest_each([("tomato", 13), ("orange", 12), ("apple", 15), ("orange", 22)])) #[('apple', 15), ('orange', 12), ('tomato', 13)]


#8. 
    #Finish the following function
def power(x, n):
    "Determine x^n recursively"
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * power(x,n-1)

print(power(2, 4)) #16
print(power(4,3)) #64
print(power(20,0)) #1


#Bonus Problem 1:
    #Finish the following function
def flatten(lst:list) -> list:
    "Write a recursive function that flattens a nested list into a single list."
    if not lst:
        return []
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return [lst[0]] + flatten(lst[1:])

print(flatten([1, [2, [3, 4]], 5])) #[1,2,3,4,5]
print(flatten([1,[2]])) #[1,2]


#Bonus Problem 2:
    #Finish the following function
def climb_stairs(n:int)->int:
    """
    A person can climb stairs 1 or 2 steps at a time. Write a 
    recursive function to find the number of ways to climb n stairs.
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(4)) #5
print(climb_stairs(6)) #13