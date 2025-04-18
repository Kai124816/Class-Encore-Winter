import copy

def remove_duplicates(lst: list[int]) -> list[int]:
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
    
    # bug HINT: Looping over an empty list means this loop never runs!
    for i in range(len(new_list)):  
        # bug HINT: 'i' is an index, but we're checking if it's in new_list instead of checking the value at i.
        if i in new_list:  
            new_list.append(new_list[i])  # bug HINT: We're appending from an empty list. Should use lst instead.
    
    return new_list


def second_largest(numbers: list[int]) -> int:
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
            largest = num  # bug HINT: second_largest is never updated correctly! It just copies largest.
            second_largest = largest  # bug HINT: This makes second_largest equal to largest instead of tracking the second largest value.
    
    return second_largest

def contains_pairs(lst: list, target: int) -> bool:
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
    # bug HINT: Typo in function name! Should be 'contains_pairs'.
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == target:
                return True  # bug HINT: This allows using the same element twice, should ensure i ≠ j.
        return False  # bug HINT: This return statement is misplaced, causing early termination.

def rotate_list(lst: list, k: int) -> list:
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
    
    # bug HINT: 'list' is a reserved keyword; should be 'lst'.
    for i in range(len(list)):
        new_list[(i - k) % len(lst)] = lst[i]  # bug HINT: This modifies new_list incorrectly; could overwrite itself.
    
    return new_list

def merge_dicts(d1: dict, d2: dict) -> dict:
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
            merged[item] = d1[item] + d2[item]  # bug HINT: This only updates existing keys but doesn't add new ones from d2.
        else:
            merged[item] = item  # bug HINT: This incorrectly assigns the key itself instead of the value!
    return merged

def invert_dict(d: dict) -> dict:
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
    new_dict = []  # bug HINT: This should be a dictionary, not a list!
    for key in d.keys():
        new_dict[key] = d[key]  # bug HINT: This doesn't swap keys and values; should be new_dict[d[key]] = key.
    return new_dict
