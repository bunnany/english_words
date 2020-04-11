##
# Sample code to use load_words.py

import load_words


def load_words():
    """ Load a list of words to a list. """ 
    return load_words.load_words()


def check_word(words, word):
    """ Check if a word exists in the list of words. """
    if word in words:
        return True
    else:
        return false


def main():
    ENGLISH_WORDS = load_words 
    print('machine' in ENGLISH_WORDS)
