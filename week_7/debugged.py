"""
on_every_line: Function takes in a word and a filename as arguments. Returns 
true if the file contains the word on each line.
"""
def on_every_line(word:str,filename:str):
    with open(filename,"r") as file:
        for line in file:
            on_line = False
            values = line.split()
            for val in values: 
                if val == word:
                    on_line = True 
            if not on_line:
                return False
    return True


"""
most_common_word: Takes a sentence as an argument and returns the word that is 
most used in that sentence
"""
def most_common_word(sentence:str):
    common_dict = {}
    sentence_list = sentence.split()
    max_apperances = 0
    max_word = None
    for word in sentence_list:
        if word not in common_dict:
            common_dict[word] = 1
        else:
            common_dict[word] += 1

        if common_dict[word] > max_apperances:
            max_apperances = common_dict[word]
            max_word = word

    return max_word


"""
sum_of_each_row: Takes a matrix as an argument and returns the a 
list where the ith element is the sum of all of the elements in the ith row.
"""
def sum_of_each_row(matrix:list[list]):
    sum_list = []
    for row in range(len(matrix)):
        sum = 0
        for col in range(len(matrix[0])):
            sum += matrix[row][col]
        sum_list.append(sum)
    return sum_list


"""
Smallest Each: From a list of (name, value) pairs, select the pairs with the smallest
value for each name.
"""
def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    smallest_dict = {}
    for pair in li:
        if pair[0] not in smallest_dict.keys():
            smallest_dict[pair[0]] = pair[1]
        elif pair[1] < smallest_dict[pair[0]]:
            smallest_dict[pair[0]] = pair[1]
    
    smallest_list = []
    for key in smallest_dict.keys():
        t1 = (key,smallest_dict[key])
        smallest_list.append(t1)

    return smallest_list


"""
What's their ranking: Function takes in a fighter's name and returns their ranking. 
For example: if I input the name Sean O'Malley into the function the function will return
13.
"""
def what_ranking(fighter_name:str,ranking_file:str):
    with open(ranking_file,"r") as file:
        for line in file:
            if line.split()[1:] == fighter_name.split():
                return f"{fighter_name} is ranked number {line.split()[0]}"
    return "fighter is not ranked in pound for pound list"


"""
largest_on_each_row: Takes a matrix as an argument and returns the a 
list where the ith element is the largest element in the ith row.
"""
def largest_on_each_row(matrix:list[list]):
    largest_list = []
    for row in range(len(matrix)):
        largest = None
        for col in range(len(matrix[0])):
            if largest == None or matrix[row][col] > largest:
                largest = matrix[row][col]
        largest_list.append(largest)
    return largest_list
