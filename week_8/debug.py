import copy

def remove_duplicates(lst:list[int]) -> list[int]:
    """
    Returns a new list with duplicates removed while maintaining order.
    
    Example:
    >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5])
    [1, 2, 3, 4, 5]
    >>> remove_duplicates(['a', 'b', 'a', 'c', 'b'])
    ['a', 'b', 'c']
    >>> remove_duplicates([])
    []
    """
    new_list = []

    for i in range(len(new_list)):
        if i in new_list:
            new_list.append(new_list[i])
    
    return new_list


def second_largest(numbers:list[int]) -> int:
    """
    Returns the second largest number in the list.
    
    Example:
    >>> second_largest([10, 20, 4, 45, 99])
    45
    >>> second_largest([5, 5, 5, 5])
    None
    >>> second_largest([1, 2])
    1
    """
    largest = numbers[0]
    second_largest = None

    for num in numbers[1:]:
        if num > largest:   
            largest = num
            second_largest = largest
    
    return second_largest


def cointains_pairs(lst:list, target:int) -> bool:
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
            if lst[i] + lst[j] == target:
                return True
        return False
    

def rotate_list(lst:list, k:int) -> list:
    """
    Rotates the list to the right by k positions and 
    returns new list representing this rotated list
    
    Example:
    >>> rotate_list([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    >>> rotate_list([10, 20, 30], 1)
    [30, 10, 20]
    >>> rotate_list([], 3)
    []
    """
    new_list = copy.deepcopy(lst)
    for i in range(len(list)):
        new_list[(i-k) % len(lst)] = lst[i]

    return new_list


def merge_dicts(d1:dict, d2:dict) -> dict:
    """
    Merges two dictionaries, summing values for common keys.
    
    Example:
    >>> merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    {'a': 1, 'b': 5, 'c': 4}
    >>> merge_dicts({}, {'x': 10})
    {'x': 10}
    >>> merge_dicts({'p': 5}, {})
    {'p': 5}
    """
    merged = copy.deepcopy(d1)
    for item in d1:
        if item in d2:
            merged[item] = d1[item] + d2[item]
        else:
            merged[item] = item
    return merged


def invert_dict(d:dict) -> dict:
    """
    Returns a new dictionary with keys and values swapped.
    
    Example:
    >>> invert_dict({'a': 1, 'b': 2, 'c': 3})
    {1: 'a', 2: 'b', 3: 'c'}
    >>> invert_dict({'x': 10, 'y': 20, 'z': 10})
    {10: 'z', 20: 'y'}
    >>> invert_dict({})
    {}
    """
    new_dict = []
    for key in d.keys():
        new_dict[key] = d[key]
    return new_dict










    


    
