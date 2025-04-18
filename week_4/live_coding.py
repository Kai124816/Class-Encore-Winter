"Problem 1: Write a function that takes a string and returns the number of vowels in it"
def count_vowels(s):
    count = 0
    vowels = "AEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count


"Problem 2: Write a function that takes a string and reverses it"



"Problem 3: Write a function that determines if a string is a palindrome"
def is_palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[(-1*i)-1]:
            return False
    return True


"Problem 4: Write a function that determines the number of words in a string."
"assume words are separated by spaces"
def number_of_words(s):
    return


"Problem 5: Decode a ciphered text that was encrypted using the even odd shuffle"
"Below is the function that encodes a text using the even odd shuffle"
def scramble_2_encrypt(plain_text):
    even_chars = ""
    odd_chars = ""
    char_count = 0
    for ch in plain_text:
        if char_count % 2 == 0:
            even_chars = even_chars + ch
        else:
            odd_chars = odd_chars + ch
            char_count = char_count + 1
            cipher_text = odd_chars + even_chars
    return cipher_text

def decode_scramble(ciphered_text):
    return


"Problem 6: Decode a given ciphered text using the provided key." 
"A helper function is provided to convert letters"
"(a → 0, b → 1, ..., z → 25). Both the ciphered text and key are lowercase."
def letter_to_value(s):
    return ord(s) - ord('a')

def value_to_letter(value):
    return chr(value + ord('a'))

def encrypt_vigenere(plain_text, key):
    key_len = len(key)
    cipher_text = ""
    for i in range(len(plain_text)):
        ch = plain_text[i]
        if ch == ' ': #do not encode spaces
            cipher_text += ch
        else:
            plain_value = letter_to_value(ch)
            key_value = letter_to_value(key[i % key_len])
            shifted_value = (plain_value + key_value) % 26
            cipher_text += value_to_letter(shifted_value)
    return cipher_text

def decode_vignere(ciphered_text,key):
    return





