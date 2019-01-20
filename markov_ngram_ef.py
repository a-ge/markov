"""Generate Markov text from text files."""

import sys

file_path = sys.argv[1]
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    return open(file_path).read()

def request():
    n_gram = int(input("How many words in your key?> "))
    return n_gram

def make_chains(text_string, n_gram):
    """Take input text as string; return dictionary of Markov chains.
    
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # words = text_string.split()
    # for i in range(len(words) - 2):
    #     pair_word = (words[i], words[i+1])
    #     chains[pair_word] = chains.get(pair_word,[]) + [words[i+2]]

    words = text_string.split()

    n_list = []


    for i in range(len(words)-n_gram):  

        n_list = words[i:i+n_gram]
        # create a key from slicing words list. slice size is determined by n_gram.

        n_tuple = tuple(n_list)
        # create a tuple out of n_list so it can be a key in a dict.

        chains[n_tuple] = chains.get(n_tuple,[]) + [words[i+n_gram]]
        # add the tuple as a key in dict chains.
        # if the key doesn't already exist, create an empty list as the value.
        # then add the next sequential word in words that comes after the last string in the key.
        
    return chains

def make_text(chains, n_gram):
    """Return text from chains."""

    words = []
    chosen_tuple = choice(list(chains.keys()))

    while chosen_tuple in chains:
        
        chosen_value = chains[chosen_tuple]

        last_word = choice(chosen_value)
        
        words.append(last_word)

        chosen_last_words = list(chosen_tuple[-n_gram+1:])
        chosen_last_words.append(words[-1])

        chosen_tuple = tuple(chosen_last_words)

    return " ".join(words)


# Open the file and turn it into one long string
input_text = open_and_read_file(file_path)

# Asks how long tuple should be
n_gram = request()

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = make_text(chains, n_gram)

print(random_text)