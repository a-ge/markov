"""Generate Markov text from text files."""

import sys

file_path = sys.argv[1]
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.
file_path = sys.argv[1] + sys.argv[2]keys())
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
    n_gram = int(input("How many words in your key?> "))

    words = text_string.split()

    n_list = []

    i = 0

    while len(n_list) < n_gram:
        n_list.append("word_" + str(i))
        i+1

   #print(n_list)
    while i in range(i,i+1):#range(0+i,i+n_gram): 
        if i == len(words):
            break
        print(i,range(i,i+1), n_gram, "test")
        n_list = words[i:len(n_list)]
        print(n_list)
        if len(n_list) == n_gram:
            print("nlist",n_list)
            n_tuple = tuple(n_list)

            chains[n_tuple] = chains.get(n_tuple,[]) + [words[i+n_gram]]
        i += 1

    #print("chains",chains)

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []

    #print("words", words)
    pair = choice(list(chains.keys()))

    #print("pair", pair)


    while pair in chains:

        value = chains[pair]

        #print("value", value)

        second_word = choice(value)
        #print("second word", second_word)
        words.append(second_word)
        #print("words",words)
        pair = (pair[1], second_word)
        #print("pair",pair)


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long st
#ring
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
