#Problem 1
def is_divisible(a,b,c):
    "This function takes in three variables a,b and c"
    "and returns true if a is divisible by b and c"
    if a % b == 0 or a % c == 0:
        return True
    return False
result = is_divisible(10,2,3)
#print(result)


#Problem 2
def compare_three_strings(a,b,c):
    "Returns true if two or more of the strings share a common character"
    for char in a:
        if char in b:
            return True
        elif char in c:
            return True
    for char in b:
        if char in c:
            return True
        
        
result = compare_three_strings("car","cat","big")
#print(result)


#Problem 3
def contains_vowel(s):
    "returns true if the string contains a vowel false if it doesn't"
    vowels = "aeiou"
    s.lower()
    for char in s:
        if char in vowels:
            return True
    return False
result = contains_vowel("thrEE")
#print(result)


#Problem 4
def count_a_in_string(s):
    count = 0
    for char in s:
        if char == "a":
            count += 1
    return ("Total count of 'a':", count) 

result = count_a_in_string("banana")
#print("Function result:", result)  # What does this print?


#Problem 5
def concatenate_vowels(s):
    "Concatanates the vowels in a string"
    result = ""
    for char in s:
        if char in "aeiouAEIOU":
            result += char  # What's wrong here?
    print(result)

output = concatenate_vowels("hello world")
print("Vowels:", output)


#Problem 6
def find_first_vowel(s):
    "finds first vowel in string or None if there are no vowels in the string"
    for char in s:
        if char in "aeiou":
            return char
    print("No vowels found")  
    return None

result = find_first_vowel("sky")
#print("First vowel:", result)


#Problem 7
def categorize_number(n):
    "Categorizes a number as positive Odd, Positive Even, Zero or a Negative"
    if n % 2 == 0 and n > 0:  
        return "Positive Odd"  
    elif n % 2 != 0 and n > 0:  
        return "Positive Even"  
    elif n < 0: 
        return "Zero"  
    else:  
        return "Negative"  


#Problem 8
def check_conditions(p, q, r):
    "takes in three integers p, q, and r. Return True if:"
    "p is greater than q and r is an even number"
    if p > q or r % 1 == 0:  
        return False  
    return True  

result = check_conditions(10,7,4)
#print(result)


