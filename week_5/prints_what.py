#problem 1
d = {'a': 1, 'b': 2, 'a': 3}
#print(d)

#problem 2
s = "PythonProgramming"
#print(s[2:10:2])

#problem 3
lst = [1, 2, 3]
lst.append([4, 5])
#print(lst)

#problem 4
lst = [10, 20, 30, 40]
#print(lst[-2])

#problem 5
lst = [44, 9, 80, 12]
val = 0
for i in range(len(lst)):
    if i % 2 == 0:
        val += lst[i]
    else:
        val -= lst[i]
#print(val)
        
#problem 6
dct = {'a':44, 'b':9, 'c':80, 'd':12}
num = 0
for key in dct.keys():
    if key == 'a' or key == 'c':
        num += dct[key]
    else:
        num -= dct[key]
#print(num)
        
#problem 7
words = ["banana", "apple", "kiwi"]
#print(sorted(words, key=len))


#Problem 8
d = {'a': 1, 'b': 2, 'c': 3}
for key in d.keys():
    if d[key] % 2 != 0:
        d[key] += 1
#print(d)

#Problem 9
def three_rail_encrypt(plaintext):
    rails = ["", "", ""]
    rail = 0
    direction = 1  # 1 for down, -1 for up

    for char in plaintext:
        rails[rail] += char
        rail += direction

        if rail == 2 or rail == 0:  # Change direction at rail 2 or rail 0
            direction *= -1

    return rails[0] + rails[1] + rails[2]

#print(three_rail_encrypt("PYTHON ROCKS"))

#Problem 10
#print(three_rail_encrypt("HelloWorld"))

#Problem 11
str1 = "hello"
str2 = ""
for i in range(len(str1)):
    if i % 2 == 0:
        str2 += str1[i]
#print(str2)