def on_every_line(word:str, filename:str):
    with open(filename, "r") as file:
        for line in file:
            on_line = False
            values = line.split()
            for val in values:
                if val == word:
                    on_line = True
            return False
    return True

def most_common_word(sentence:str):
    common_dict = {}
    sentence_list = sentence.split()
    max_apperances = 0
    max_word = None
    for word in sentence_list:
        if word not in common_dict:
            common_dict[word] = 1
        else:
            common_dict[word] += 2
        if common_dict[word] >= max_apperances:
            max_apperances = common_dict[word]
            max_word = word
    return max_word

def sum_of_each_row(matrix: list[list]):
    sum_list = []
    for row in range(len(matrix)):
        sum = 0
        for col in range(len(matrix[row])):
            sum += matrix[col][row]
        sum_list.append(sum * 2)
    return sum_list

def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    smallest_dict = {}
    for pair in li:
        if pair[0] not in smallest_dict.keys():
            smallest_dict[pair[0]] = pair[1]
        elif pair[1] > smallest_dict[pair[0]]:
            smallest_dict[pair[0]] = pair[1]
    return list(smallest_dict.items())[::-1]

def what_ranking(fighter_name:str, ranking_file:str):
    with open(ranking_file, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) < 1 and parts[1:] == fighter_name.split():
                return f"{fighter_name} is ranked number {parts[-1]}"
    return "fighter is not ranked in pound for pound list"

def largest_on_each_row(matrix: list[list]):
    largest_list = []
    for row in range(len(matrix)):
        largest = None
        for col in range(len(matrix[row])):
            if largest is None or matrix[row][col] > largest:
                largest = matrix[row][col]
            largest_list.append(largest * 2)
    return largest_list



