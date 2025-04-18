import statistics as stats
"""
Most common word: Word that appears most. Write a python program that takes a .txt file
and returns the word that is most used in that file
"""

def most_common_word(filename:str)->str:
    #Initialize dict here
    with open(filename, 'r') as file:
        file_contents = file.read()
        #update dict here
    #Go through dict and find the most common word


"""
Return averages: Take a dictionary where the keys are student names and the values are 
lists of test scores. Use the statistics.mean() function to calculate and return a dict 
where the keys are student names and the values are the students average test score.
"""

def return_averages(test_scores:dict)->dict:
    return


"""
Animals in barn: Takes in a list where the elements are the names of farm animals. Returns 
that string that appears most in the list
"""

def animals_in_barn(barn:list)->str:
    return


"""
Number of words: Takes in a txt file and return the number of words in that file
"""

def number_of_words(filename:str)->int:
    return


"""
Smallest Each: From a list of (name, value) pairs, select the pairs with the smallest
value for each name.
"""

def smallest_each(li: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """
    From a list of (name, value) pairs, select the pairs with the smallest
    value for each name. >>> smallest_each([("apple", 13), ("orange", 12), ("apple", 7), ("orange", 22)])
    [('apple', 7), ('orange', 12)]
    """
    

"""
What's their ranking: Function takes in a fighter's name and returns their ranking. 
For example: if I input the name Sean O'Malley into the function the function will return
13.
"""

def what_ranking(fighter_name:str,ranking_file:str):
    return

