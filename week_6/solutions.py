
def most_common_word(filename:str)->str:
    word_dict = {}
    with open(filename,"r") as file:
        for line in file:
            values = line.split()
            for word in values: 
                if word in word_dict.keys():
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    max_word = None
    for word in word_dict.keys():
        if max_word == None:
            max_word = word
        elif word_dict[word] > word_dict[max_word]:
            max_word = word
    return max_word

def number_of_words(filename:str)->int:
    with open(filename, 'r') as file:
        file_contents = file.read().split()
    
    count = 0
    for word in file_contents:
        count += 1
    return count

def what_ranking(fighter_name:str,ranking_file:str):
    name_list = fighter_name.split()
    with open(ranking_file,"r") as file:
        for line in file:
            values = line.split()
            if values[1] == name_list[0] and values[2] == name_list[1]:
                return values[0]

print(what_ranking("Alexander Volkanovski","pound_for_pound.txt"))