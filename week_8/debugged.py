from typing import List, Dict, Optional
import copy

def remove_duplicates(lst: List[int]) -> List[int]:
    """
    Returns a new list with duplicates removed while maintaining order.
    """
    new_list = []
    
    for item in lst:  # Iterate through lst instead of an empty new_list
        if item not in new_list:
            new_list.append(item)
    
    return new_list


def second_largest(numbers: List[int]) -> Optional[int]:
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

    return second_largest if second_largest != float('-inf') else None


def contains_pairs(lst: List[int], target: int) -> bool:
    """
    Returns True if a pair of elements in the list sum to the target.
    """
    seen = set()
    
    for num in lst:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False


def rotate_list(lst: List[int], k: int) -> List[int]:
    """
    Rotates the list to the right by k positions.
    """
    if not lst:
        return []
    
    k = k % len(lst)  # Ensure k is within bounds
    return lst[-k:] + lst[:-k]


def merge_dicts(d1: Dict, d2: Dict) -> Dict:
    """
    Merges two dictionaries, summing values for common keys.
    """
    merged = d1.copy()
    
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value  # Use get() to handle missing keys
    
    return merged


def invert_dict(d: Dict) -> Dict:
    """
    Returns a new dictionary with keys and values swapped.
    """
    new_dict = {}
    
    for key, value in d.items():
        new_dict[value] = key  # Overwrites duplicate values (intentional)
    
    return new_dict
