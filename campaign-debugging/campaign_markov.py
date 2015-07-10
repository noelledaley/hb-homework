# changed import argv to import sys
import sys
from random import choice


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    chains = {}

    words = corpus.split()

    # Have to change index to - 2 to avoid index error
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            # added [value], otherwise would've returned empty list
            chains[key] = [value]
        else:
            # append(), not add() since this is a list
            chains[key].append(value)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    chain_keys = chains.keys()
    key = chain_keys[0]
    words = [key[0], key[1]]
    count = 0

    # Keep doing this until we reach the end or until we go too
    # long for a Twitter message
    while key in chains and count < 140:

        word = choice(chains[key])
        count += len(word)
        words.append(word)
        key = (key[1], word)

    return " ".join(words)


input_path = sys.argv[1]
input_text = open(input_path).read()

# changed to input_text since input_path is not a file object
chains = make_chains(input_text)

random_text = make_text(chains)

print random_text
