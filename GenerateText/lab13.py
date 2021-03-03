#Lab 13
#Danny Grimmig


import random

# Function completed for you
def read_word_list(fname):
    '''
    Reads in a specified file and returns a list of all words in the file
    in the order that they appear.
    
    Args:
        fname (str): the name of the file to read in
    Returns:
        (list of str) - a list containing each word read in from
        the file (in order).
    '''

    # Use UTF8 character encoding to read from Project Gutenberg text files
    f = open(fname, "r", encoding="utf-8-sig")

    all_words = []
    for line in f:
        word_list = line.split()
        all_words += word_list

    f.close()
    return all_words

# Function completed for you
def get_random_word(word_list):
    '''
    Given a list of words, return one word at random
    
    Args:
        word_list (list of str): a list of words
    Returns:
        (str) - one word, at random, from the list
    '''
    return word_list[random.randrange(0,len(word_list))]

# ********** Complete all the functions below! **********

def build_next_words_dictionary(all_words):
    '''
    Given a list of words, create a dictionary where each word in that list is
    a key and the value is a list of all words that have appeared
    immediately after that word
    .
    Args:
        all_words (list of str): a list of words
    Returns:
        (dict mapping (str) keys to (list of str) values)) -
            the dictionary of words and list of all possible words that could
            follow
    '''
    my_dict = {}
    for words in range(len(all_words)):
        if (words + 1) != len(all_words):
            current = all_words[words]
            next_word = all_words[words + 1]                #for each word, create a list of values of possible next words by using .get
            my_dict[current] = my_dict.get(current,[]) + [next_word]
    return(my_dict) #returns the dictionary, takes super long time!!
    
    
def make_word_sequence(next_words, num_words, start_word):
    '''
    With dictionary of words mapped to the list of words that might follow,
    generate a sequence of words where the last word is always used to generate the
    next word. 

    Args:
        next_words (dict mapping (str) keys to (list of str) values)):
            the dictionary of words and list of all possible words that could
            follow
        num_words (int): The number of words to include in the generated sequence
        start_word (str): The first word in the sequence
    Returns:
        (str) - The generated sequence, a single string with each word separated
            by a space
    '''
    first = start_word
    d = next_words
    sequence = [start_word]
    for i in range(num_words - 1):      #starts with random word, then from there gets list of possible next words
        my_list = []
        current_word = sequence[i]      #plug this list into get random word generator
        for word in (d[current_word]):  #make next word the new current word, repeat until num words desired
            my_list.append(word)   
        next_word = get_random_word(my_list)
        sequence.append(next_word)
    string = ''
    for j in sequence:
        string+= j + ' '
    return(string)  #take the list made above and convert to a string
    
def generate_text(string):
    '''
    takes the new computer generated string and turns it into a txt file
    '''
    with open("generated_text.txt", "w") as f:
        f.write(string)


def main():
    all_words = read_word_list("frankenstein.txt") #calls all above functions to perform task!
    next_words = build_next_words_dictionary(all_words)
    num_words = int(input("How many words : "))
    start_word = get_random_word(all_words)
    word_sequence = make_word_sequence(next_words, num_words, start_word)
    generate_text(word_sequence)

main()
    
    


    

