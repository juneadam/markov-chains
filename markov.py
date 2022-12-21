"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_string = open(file_path).read()
    # read method on file
    # open_file = open_file.read()
    text_string = text_string.replace('\n', " ")
    text_string = text_string.replace('\r', " ")
    
    return text_string
    # 'Contents of your file as one long string'

# open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

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

    words_list = text_string.split()
    # print(words_list)
    for i, word in enumerate(words_list):
        if i == len(words_list) - 2:
            break
        if chains.get((words_list[i], words_list[i + 1]), 0) == 0:
            chains[(words_list[i], words_list[i + 1])] = [words_list[i+2]]
        # if the bigram does not exist in dictionary, append
        if chains.get((words_list[i], words_list[i + 1]), 0) != 0:
            chains[(words_list[i], words_list[i + 1])].append(words_list[i + 2])
        # if chains.get((words_list[i], words_list)
    return chains

# print(make_chains(open_and_read_file("green-eggs.txt")))

def make_text(chains):
    """Return text from chains."""
   
    words = []
    random_value = ''
    # turn chains.keys() to list
    keys_list = list(chains.keys())

    random_key = choice(keys_list)

    words.append(random_key[0])
    words.append(random_key[1])

    # for key, value in chains.items():
    while True:    
        random_value = choice(chains[random_key])
        # break loop if keyerror
        # if random_value == 'KeyError':
        #     break
        random_key = (random_key[1], random_value)
        words.append(random_value)
        if chains.get(random_key, 0) == 0:
            break
        
    return ' '.join(words)

input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print(open_and_read_file(input_path))

# Get a Markov chain
chains = make_chains(input_text)
print(make_chains(input_text))

# Produce random text
random_text = make_text(chains)

print(random_text)
