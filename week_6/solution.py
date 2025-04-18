
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

